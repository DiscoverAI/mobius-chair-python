import metron.core as m
from metron.filesystem import *


def test_find_latest_dataset():
    metron = m.Metron(LocalFileSystem(), "test-resources/filesystem/zipper")
    assert sorted(metron.get_latest_dataset()) == ["test-resources/filesystem/zipper/0002/0002/your_dataset.csv",
                                                   "test-resources/filesystem/zipper/0002/0002/your_dataset2.csv"]
