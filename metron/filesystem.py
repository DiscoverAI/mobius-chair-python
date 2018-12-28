import abc
import os


class FileSystem(abc.ABC):
    def list_directories(self, path):
        pass

    def file_exists(self, path):
        pass

    def get_all_files(self, path):
        pass


class LocalFileSystem(FileSystem):
    def list_directories(self, path):
        print(os.getcwd())
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

    def file_exists(self, path):
        return os.path.isfile(path)

    def get_all_files(self, path):
        return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


class HadoopFileSystem(FileSystem):
    pass

class AmazonS3FileSystem(FileSystem):
    pass