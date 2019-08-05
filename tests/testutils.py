from hdfs import Client
import shutil
import os


class MockClient(Client):
    def __init__(self):
        super().__init__("")

    def delete(self, hdfs_path, recursive=False, skip_trash=True):
        shutil.rmtree(hdfs_path)

    def list(self, hdfs_path, status=False):
        return os.listdir(hdfs_path)

    def status(self, hdfs_path, strict=True):
        if not os.path.exists(hdfs_path) and strict == False:
            return None
        elif os.path.isdir(hdfs_path):
            return {'type': "DIRECTORY"}
        else:
            return {'type': "FILE"}

    def makedirs(self, hdfs_path, permission=None):
        os.makedirs(hdfs_path)

    def walk(self, hdfs_path, depth=0, status=False, ignore_missing=False):
        if depth == 1:
            for item in os.listdir(hdfs_path):
                if not os.path.isfile(hdfs_path + "/" + item):
                    yield item, None, None


test_fs = MockClient()

fs_path = os.path.join(os.getcwd(), "test-resources/filesystem")
zipper_base_path = fs_path + "/" + "zipper"
