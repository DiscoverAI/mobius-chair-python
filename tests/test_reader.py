from tests.testutils import *
import mobius_chair.reader as r


def test_generation_already_processed():
    assert r.generation_already_processed(test_fs, zipper_base_path + "/0001/0001")
    assert not r.generation_already_processed(test_fs, zipper_base_path + "/0002/0002")


def test_get_dataset_generations():
    sorted_generations = r.get_sorted_dataset_generations(test_fs, base_path=fs_path, app_name="zipper",
                                                          app_version="0001")
    assert sorted_generations == \
           [zipper_base_path + "/0001/0012",
            zipper_base_path + "/0001/0010",
            zipper_base_path + "/0001/0002",
            zipper_base_path + "/0001/0001"]


def test_get_all_dataset_files():
    assert r.get_all_files_except_success_file(test_fs, zipper_base_path + "/0001/0001") == \
           [zipper_base_path + "/0001/0001/dataset.csv"]
    assert r.get_all_files_except_success_file(test_fs, zipper_base_path + "/0001/0002") == []


def test_get_latest_dataset():
    latest_dataset = r.get_latest_dataset(test_fs, base_path=fs_path, app_name="zipper")
    assert sorted(latest_dataset) == \
           [zipper_base_path + "/0002/0002/your_dataset.csv",
            zipper_base_path + "/0002/0002/your_dataset2.csv"]
