import os
import re

version_format = "^.*/\\d{4}$"


def common_number_format(integer):
    return '{:0>4d}'.format(integer)


def get_generations(fs, base_path):
    generations = [path for path in fs.ls(base_path) if fs.isdir(path)]
    generations = [path for path in generations if re.match(version_format, path)]
    return generations


def sort_by_generation(paths, reverse=False):
    return sorted(paths, reverse=reverse, key=lambda path: int(os.path.basename(path)))
