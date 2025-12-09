
# Loads directory structure from JSON and builds Directory/File objects
import json
from app.filesystem import Directory, File

# Recursively build Directory tree from dict
def build_directory(data):
    d = Directory(data["name"])
    for f in data.get("files", []):
        d.add_file(File(f["name"], f["size"]))  # Add each file to directory
    for sub in data.get("directories", []):
        child = build_directory(sub)  # Recursively build subdirectories
        d.add_subdir(child)
    return d

# Loads the root directory from a JSON file (default: data/seed.json)
def load_from_json(path="data/seed.json"):
    """Load the root directory from a JSON file and build the directory tree."""
    with open(path, "r") as f:
        data = json.load(f)
    return build_directory(data)