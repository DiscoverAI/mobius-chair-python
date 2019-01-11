import os
import re
import logging

version_format = "^.*/\\d{4}$"


def common_number_format(integer):
    return '{:0>4d}'.format(integer)


def sort_by_generation(paths):
    return sorted(paths, key=lambda path: int(os.path.basename(path)))


def get_generations(fs, base_path):
    generations = [path for path in fs.ls(base_path) if fs.isdir(path)]
    generations = [path for path in generations if re.match('^.*/\\d{4}$', path)]
    return generations


def output_path(fs, base_path, name, version):
    job_output_path = base_path + fs.pathsep + name + fs.pathsep + common_number_format(int(version))
    if create_if_not_available(fs, job_output_path):
        logging.info("Output folder was created")
    generation = next_generation(fs, base_path)
    return job_output_path + fs.pathsep + generation


def latest_generation(fs, base_path):
    generations = [int(os.path.basename(path)) for path in get_generations(fs, base_path)]
    return common_number_format(max(generations)) if len(generations) > 0 \
        else logging.warning("Did not find latest generation")


def next_generation(fs, base_path):
    current_generation = latest_generation(fs, base_path)
    return common_number_format(int(current_generation) + 1 if current_generation is not None else 1)


def clean_up_generations(fs, base_path, num_to_keep):
    generation_paths = get_generations(fs, base_path)
    sorted_generations = sort_by_generation(generation_paths)
    for path in sorted_generations[:-num_to_keep]:
        fs.delete(path)


def create_if_not_available(fs, path):
    if not fs.exists(path):
        fs.mkdir(path, create_parents=True)
        return True
    return False
