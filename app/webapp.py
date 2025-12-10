import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template, request, jsonify
from app.filesystem import Directory, File
from app.shell import Shell
from app.loader import load_from_json

# Initialize Flask app
app = Flask(__name__)

# Build the file system from seed.json (real data)
# This ensures the web UI uses the same data as the CLI
root = load_from_json()  # Loads the directory tree from data/seed.json
shell = Shell(root)      # Shell object to track current directory
shell.current = root

# Home page route: serves the UI
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint for running commands from the UI
@app.route("/command", methods=["POST"])
def command():
    cmd = request.json.get("cmd", "")
    output = ""
    # Handle supported commands
    if cmd == "ls":
        output = "\n".join(shell.current.list_contents())
    elif cmd.startswith("cd"):
        parts = cmd.split()
        if len(parts) == 2:
            target = parts[1]
            if target == "..":
                if shell.current.parent:
                    shell.current = shell.current.parent
                    output = f"Moved to {shell.current.name}"
                else:
                    output = "Already at root"
            else:
                new_dir = shell.current.get_subdir(target)
                if new_dir:
                    shell.current = new_dir
                    output = f"Moved to {shell.current.name}"
                else:
                    output = "Directory not found"
        else:
            output = "Usage: cd <directory>"
    elif cmd == "size":
        # Recursively calculate total size
        output = f"Total size: {shell.current.calculate_size()} KB"
    else:
        output = "Unknown command"
    return jsonify({"output": output, "cwd": shell.current.name})

# Run the Flask development server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)