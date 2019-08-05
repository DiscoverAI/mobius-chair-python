import os
import re

version_format = "^\d{4}$"


def common_number_format(integer):
    return '{:0>4d}'.format(integer)


def get_generations(fs, path_to_version):
    dir_contents = fs.list(path_to_version)
    generations = [filename for filename in dir_contents if
                   fs.status(path_to_version + "/" + filename)['type'] == "DIRECTORY"]
    generations = [path_to_version + "/" + filename for filename in generations if re.match(version_format, filename)]
    return generations


def sort_by_generation(paths, reverse=False):
    return sorted(paths, reverse=reverse, key=lambda path: int(os.path.basename(path)))
