from app.filesystem import Directory, File
from app.shell import Shell

def test_cd_and_ls():
    root = Directory("/")
    sub = Directory("docs")
    root.add_subdir(sub)

    shell = Shell(root)
    shell.current = root

    assert shell.current.get_subdir("docs") == sub
