from mobius_chair.utility import *


def generation_already_processed(fs, path_to_generation):
    return fs.status(path_to_generation + "/_SUCCESS", strict=False) is not None


def get_sorted_dataset_generations(fs, base_path, app_name, app_version):
    path_to_transformation_version = "/".join((base_path, app_name, app_version))
    return sort_by_generation(get_generations(fs, path_to_transformation_version), reverse=True)


def get_all_files_except_success_file(fs, path_to_generation):
    return [path_to_generation + "/" + f
            for f in fs.list(path_to_generation)
            if os.path.basename(path_to_generation + "/" + f) != '_SUCCESS']


def _list_folders(fs, path):
    return sort_by_generation([path for path, _subdirs, _files in fs.walk(path, depth=1)], reverse=True)


def get_latest_dataset(fs, base_path, app_name):
    for version_path in sort_by_generation(_list_folders(fs, base_path + "/" + app_name), reverse=True):
        version = os.path.basename(version_path)
        path_to_version = base_path + "/" + app_name + "/" + version
        for path_to_generation in get_generations(fs, path_to_version):
            if not generation_already_processed(fs, path_to_generation):
                return get_all_files_except_success_file(fs, path_to_generation)
