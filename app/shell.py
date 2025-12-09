class Shell:
    """
    Command-line shell for navigating and interacting with the in-memory file system.
    Supports commands: ls, cd <dir>, size, exit.
    """
    def __init__(self, root):
        self.root = root           # Root directory of the file system
        self.current = root        # Current working directory

    def run(self):
        print("Directory Size Calculator Shell")
        print("Commands: ls, cd <dir>, size, exit")

        while True:
            cmd = input(f"{self.current.name}> ").strip()

            if cmd == "exit":
                break

            elif cmd == "ls":
                # List contents of the current directory
                items = self.current.list_contents()
                for item in items:
                    print(item)

            elif cmd.startswith("cd"):
                # Change directory (cd <dir> or cd ..)
                parts = cmd.split()

                if len(parts) == 1:
                    print("Usage: cd <directory>")
                    continue

                target = parts[1]

                if target == "..":
                    # Move up to parent directory
                    if self.current.parent:
                        self.current = self.current.parent
                    else:
                        print("Already at root")
                    continue

                new_dir = self.current.get_subdir(target)
                if new_dir:
                    self.current = new_dir
                else:
                    print("Directory not found")

            elif cmd == "size":
                # Calculate total size of current directory (recursive)
                size = self.current.calculate_size()
                print(f"Total size: {size} KB")

            else:
                print("Unknown command")