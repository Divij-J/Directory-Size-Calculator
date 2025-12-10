# Directory Size Calculator (Python)

## Overview
This is a command-line application that simulates a simple hierarchical file system in memory.  
The user can navigate directories, list contents, and calculate total directory size using recursion.

**Commands supported:**
- `ls` – list contents of current directory  
- `cd <directory>` – move into a directory  
- `cd ..` – go up one level  
- `size` – recursively compute total size  
- `exit` – quit the program  

---

## Approach & Design
### 1. In-Memory File System
The application uses a **tree structure**:
- Each folder is a `Directory` object.
- Each file is a `File` object with a size attribute.
- Directories contain:
  - A list of subdirectories  
  - A list of files  
  - A pointer to their parent (for `cd ..`)

### 2. Recursion for Directory Size
The `calculate_size()` function:
- Sums sizes of all files in the directory
- Recursively calls itself on each subdirectory  
- Returns the total

This efficiently simulates how real filesystems compute usage.

### 3. Command-Line Interface (Shell)
- All commands run through the `Shell` class.
- Input is parsed into actions (cd, ls, size).
- State is tracked with `self.current`, pointing to the active directory.

### 4. Seed Data
A sample filesystem structure is stored in `data/seed.json` and loaded automatically.

---


## Key Files & Folders

| File/Folder | Description |
|-------------|-------------|
| `app/filesystem.py` | Core classes for File and Directory |
| `app/shell.py` | Command interpreter for CLI |
| `app/loader.py` | Loads directory tree from JSON |
| `app/webapp.py` | Flask web server for UI |
| `app/templates/index.html` | Web UI frontend |
| `data/seed.json` | Seed data for the filesystem |
| `main.py` | CLI entry point |
| `requirements.txt` | Dependencies |
| `tests/` | Unit tests |

---
## How to Run

Clone the repo:
git clone <your-repo-url>
cd directory-size-calculator



Run the command-line application:
pip install -r requirements.txt
python main.py

---

## Web UI (Flask) Version

To run the web-based UI:

1. Install requirements (if not already done):
  ```
  pip install -r requirements.txt
  ```
2. Start the web server:
  ```
  python app/webapp.py
  ```
3. Open your browser and go to [http://localhost:5000](http://localhost:5000)

You can enter commands (`ls`, `cd <dir>`, `size`) in the web interface and see the output instantly.

---
## Hosted Version

The app is deployed and publicly accessible at:
**https://directory-size-calculator.onrender.com**

You can use all commands (`ls`, `cd <dir>`, `size`) directly in the browser.

Example usage:

/> ls
/> cd documents
/documents> size
/documents> cd ..
/> exit

---
## Test & Verification

Run tests:

pytest

Tests cover:
- Directory size recursion  
- Subdirectory access  
- Basic shell navigation  
---
## Seed Data

`data/seed.json` includes:
- 2 top-level folders  
- nested subdirectories  
- files with realistic sizes  

This allows quick verification of:
- navigation  
- listing  
- size calculations  

---

## Additional Notes
- No database is used; everything runs in memory.
- Code is modular and easy to extend with new commands.
- A hosted version and instructions are included in PRESENTATION.md.

