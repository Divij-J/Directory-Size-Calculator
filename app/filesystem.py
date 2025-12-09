
class File:
    """
    Represents a file with a name and size (in KB).
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size  # size in KB

    def __repr__(self):
        return f"{self.name} ({self.size} KB)"

class Directory:
    """
    Represents a directory (folder) that can contain files and subdirectories.
    Supports recursive size calculation and navigation.
    """
    def __init__(self, name):
        self.name = name
        self.subdirs = []      # List of subdirectories
        self.files = []        # List of files in this directory
        self.parent = None     # Reference to parent directory (for cd ..)

    def add_subdir(self, directory):
        directory.parent = self
        self.subdirs.append(directory)

    def add_file(self, file):
        self.files.append(file)

    def get_subdir(self, name):
        # Find a subdirectory by name
        for d in self.subdirs:
            if d.name == name:
                return d
        return None

    def list_contents(self):
        # List all subdirectories and files in this directory
        dirs = [d.name + "/" for d in self.subdirs]
        files = [f"{f.name} ({f.size} KB)" for f in self.files]
        return dirs + files

    def calculate_size(self):
        # Recursively calculate total size (files + all subdirectories)
        total = sum(f.size for f in self.files)
        for sub in self.subdirs:
            total += sub.calculate_size()
        return total