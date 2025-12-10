# Directory Size Calculator – Short Presentation

## 1. Approach & Design

### In-Memory Tree Structure
- Each directory is a node with:
  - Subdirectories
  - Files
  - Parent reference
- Each file has a name + size.
- This forms a hierarchical tree similar to a real file system.

### Recursive Size Calculation
- Each directory computes its size by:
  - Summing its files
  - Recursively summing all child directories

### Command-Line Interface
- A simple shell interprets commands:
  - `ls`, `cd`, `cd ..`, `size`, `exit`
- State is managed through the current directory pointer.

---


## 2. Key Files & Folders
- `app/filesystem.py` — core classes for File and Directory
- `app/shell.py` — command interpreter for CLI
- `app/loader.py` — loads directory tree from JSON
- `app/webapp.py` — Flask web server for UI
- `app/templates/index.html` — Web UI frontend
- `data/seed.json` — seed data for the filesystem
- `main.py` — CLI entry point
- `requirements.txt` — dependencies
- `tests/` — unit tests

### Project File Tree
```
Directory-Size-Calculator/
├── app/
│   ├── filesystem.py
│   ├── loader.py
│   ├── shell.py
│   ├── webapp.py
│   └── templates/
│       └── index.html
├── data/
│   └── seed.json
├── tests/
│   ├── test_filesystem.py
│   └── test_shell.py
├── main.py
├── requirements.txt
├── readme.md
└── presentation.md
```

---

## 3. How to Run, Test, and Verify

### Run Locally
```bash
pip install -r requirements.txt
python main.py
```
### Web UI (Flask)
```bash
python app/webapp.py
```
Visit [http://localhost:5000](http://localhost:5000)

### Hosted Version
The app is deployed at:
**https://directory-size-calculator.onrender.com**
Use all commands (`ls`, `cd <dir>`, `size`) in the browser.

### Test
```bash
pytest

### Verify
- Use `ls` to list files and directories.
- Use `cd` and `cd ..` to navigate into nested directories.
- Use `size` in different directories and verify that:
  - Sizes match the sum of files in that directory and its subdirectories.
  - Sizes match expectations from `data/seed.json`.
---

## 4. Included Test & Seed Data
- `seed.json` provides initial folders & files  
- `tests/` includes checks for:
  - recursion  
  - navigation  
  - command shell behavior  