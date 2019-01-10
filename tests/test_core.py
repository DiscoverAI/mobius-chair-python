from mobius_chair.core import MobiusChair
from mobius_chair.filesystem import LocalFileSystem


def test_find_latest_dataset():
    mobius_chair = MobiusChair(LocalFileSystem(), "test-resources/filesystem/zipper")
    expected = [
        "test-resources/filesystem/zipper/0002/0002/your_dataset.csv",
        "test-resources/filesystem/zipper/0002/0002/your_dataset2.csv"
    ]

    assert expected == sorted(mobius_chair.get_latest_dataset())
