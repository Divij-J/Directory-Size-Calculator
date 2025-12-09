# Entry point for CLI app. Loads file system and starts shell.
from app.loader import load_from_json
from app.shell import Shell


def main():
    root = load_from_json()  # Loads directory tree from data/seed.json
    shell = Shell(root)      # Starts shell with root directory
    shell.run()             # Runs command-line interface

if __name__ == "__main__":
    main()
