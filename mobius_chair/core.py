import os
import re
import logging


def common_number_format(integer):
    return '{:0>4d}'.format(integer)


def output_path(fs, base_path, name, version):
    job_output_path = base_path + fs.pathsep + name + fs.pathsep + common_number_format(int(version))
    logging.warning("JOB OUTPUT PATH" + base_path)
    if create_if_not_available(fs, job_output_path):
        logging.info("Output folder was created")
    generation = next_generation(fs, base_path)
    return job_output_path + fs.pathsep + generation


def latest_generation(fs, base_path):
    generations = [path for path in fs.ls(base_path) if os.path.isdir(path)]
    generations = [path for path in generations if re.match('^\\d+$', os.path.basename(path))]
    generations = [int(os.path.basename(path)) for path in generations]
    return common_number_format(max(generations)) if len(generations) > 0 \
        else logging.warning("Did not find latest generation")


def next_generation(fs, base_path):
    current_generation = latest_generation(fs, base_path)
    return common_number_format(int(current_generation) + 1 if current_generation is not None else 1)


def clean_up_generations(fs_uri, base_path, num_to_keep):
    pass


def create_if_not_available(fs, path):
    if not fs.exists(path):
        fs.mkdir(path, create_parents=True)
        return True
    return False
