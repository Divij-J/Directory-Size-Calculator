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
- `app/filesystem.py` — core classes  
- `app/shell.py` — command interpreter  
- `app/loader.py` — loads JSON seed data  
- `data/seed.json` — sample filesystem  
- `main.py` — entry point  
- `tests/` — unit tests  

---

## 3. How to Run, Test, and Verify

### Run
main.py

### Test
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

---

## Optional Hosted Version
A hosted version may be provided using:

