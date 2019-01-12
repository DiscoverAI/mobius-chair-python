from pyarrow import LocalFileSystem
import shutil
import os

test_fs = LocalFileSystem()
# pyarrow LocalFileSystem does not implement delete
# but HadoopFileSystem, the actual implementation you will be working with, does.
test_fs.delete = lambda x: shutil.rmtree(x)

fs_path = os.path.join(os.getcwd(), "test-resources/filesystem")
zipper_base_path = fs_path + "/" + "zipper"
