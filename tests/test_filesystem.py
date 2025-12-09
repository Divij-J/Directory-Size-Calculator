from app.filesystem import Directory, File

def test_directory_size():
    root = Directory("root")
    root.add_file(File("a", 10))
    sub = Directory("sub")
    sub.add_file(File("b", 5))
    root.add_subdir(sub)

    assert root.calculate_size() == 15
