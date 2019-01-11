import mobius_chair.core as mc
from pyarrow import LocalFileSystem
import os
import logging

test_fs = LocalFileSystem()
fs_path = os.path.join(os.getcwd(), "test-resources/filesystem")
zipper_base_path = fs_path + "/" + "zipper"
logging.warning(zipper_base_path)


def test_get_latest_generation():
    latest_gen = mc.latest_generation(test_fs, zipper_base_path + "/0001")
    assert latest_gen == "0010"
    latest_gen = mc.latest_generation(test_fs, zipper_base_path + "/0002")
    assert latest_gen == "0002"


def test_next_generation():
    next_gen = mc.next_generation(test_fs, zipper_base_path + "/0001")
    assert next_gen == "0011"
    next_gen = mc.next_generation(test_fs, zipper_base_path + "/0002")
    assert next_gen == "0003"
    next_gen = mc.next_generation(test_fs, zipper_base_path + "/0003")
    assert next_gen == "0001"


def test_create_if_not_available():
    some_dir = os.path.join(os.getcwd(), "test-dir")
    was_created = mc.create_if_not_available(test_fs, some_dir)
    assert was_created
    os.rmdir(some_dir)
    was_created = mc.create_if_not_available(test_fs, zipper_base_path)
    assert not was_created


def test_get_output_path():
    output_path = mc.output_path(test_fs, fs_path, "zapper", 4)
    expected_dir = fs_path + "/zapper/0004/0001"
    assert output_path == expected_dir
    os.rmdir(fs_path + "/zapper/0004")
    os.rmdir(fs_path + "/zapper")
