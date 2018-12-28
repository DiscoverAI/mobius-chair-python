import os


class Metron:
    def __init__(self, filesystem, base_path):
        self.filesystem = filesystem
        self.base_path = base_path

    def get_dataset_generations(self, transformation_version):
        path_to_transformation_version = os.path.join(self.base_path, transformation_version)
        return sorted(self.filesystem.list_directories(path_to_transformation_version), reverse=True)

    def generation_already_processed(self, path_to_generation):
        return self.filesystem.file_exists(path_to_generation + "/_SUCCESS")

    def get_all_files_except_success_file(self, path_to_generation):
        return [f for f in self.filesystem.get_all_files(path_to_generation) if not "_SUCCESS" in f]

    def find_latest(self, transformation_version):
        for gen in self.get_dataset_generations(transformation_version):
            path_to_generation = os.path.join(self.base_path, transformation_version, gen)
            if not self.generation_already_processed(path_to_generation):
                return self.get_all_files_except_success_file(path_to_generation)

    def get_latest_dataset(self):
        transformation_versions = sorted(self.filesystem.list_directories(self.base_path), reverse=True)
        for v in transformation_versions:
            latest = self.find_latest(v)
            if latest:
                return latest
