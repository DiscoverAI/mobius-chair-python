from metron.filesystem import *


def test_local_filesystem():
    local_fs = LocalFileSystem()
    assert sorted(local_fs.list_directories("test-resources/filesystem/zipper")) == ["0001", "0002"]
    assert local_fs.file_exists("test-resources/filesystem/zipper/0001/0007/_SUCCESS")
    assert sorted(local_fs.get_all_files("test-resources/filesystem/zipper/0002/0002/")) \
           == ["test-resources/filesystem/zipper/0002/0002/your_dataset.csv",
               "test-resources/filesystem/zipper/0002/0002/your_dataset2.csv"]
