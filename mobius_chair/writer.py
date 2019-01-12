import logging
from mobius_chair.utility import *


def output_path(fs, base_path, name, version):
    job_output_path = base_path + fs.pathsep + name + fs.pathsep + common_number_format(int(version))
    if _create_if_not_available(fs, job_output_path):
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


def _create_if_not_available(fs, path):
    if not fs.exists(path):
        fs.mkdir(path, create_parents=True)
        return True
    return False
