from mobius_chair.utility import *


def generation_already_processed(fs, path_to_generation):
    return fs.exists(path_to_generation + "/_SUCCESS")


def get_sorted_dataset_generations(fs, base_path, app_name, app_version):
    path_to_transformation_version = os.path.join(base_path, app_name, app_version)
    return sort_by_generation(get_generations(fs, path_to_transformation_version), reverse=True)


def get_all_files_except_success_file(fs, path_to_generation):
    return [f for f in fs.ls(path_to_generation) if os.path.basename(f) != '_SUCCESS']


def get_latest_dataset(fs, base_path, app_name, compatible_versions):
    for version in sorted([int(v) for v in compatible_versions.split(",")], reverse=True):
        path_to_version = base_path + fs.pathsep + app_name + fs.pathsep + common_number_format(version)
        for path_to_generation in fs.ls(path_to_version):
            if not generation_already_processed(fs, path_to_generation):
                return get_all_files_except_success_file(fs, path_to_generation)

