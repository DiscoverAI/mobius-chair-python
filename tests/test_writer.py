import mobius_chair.writer as mc
from tests.testutils import *


def test_get_latest_generation():
    latest_gen = mc.latest_generation(test_fs, zipper_base_path + "/0001")
    assert latest_gen == "0012"
    latest_gen = mc.latest_generation(test_fs, zipper_base_path + "/0002")
    assert latest_gen == "0002"


def test_next_generation():
    next_gen = mc.next_generation(test_fs, zipper_base_path + "/0001")
    assert next_gen == "0013"
    next_gen = mc.next_generation(test_fs, zipper_base_path + "/0002")
    assert next_gen == "0003"
    next_gen = mc.next_generation(test_fs, zipper_base_path + "/0003")
    assert next_gen == "0001"


def test_create_if_not_available():
    some_dir = os.path.join(os.getcwd(), "test-dir")
    was_created = mc._create_if_not_available(test_fs, some_dir)
    assert was_created
    os.rmdir(some_dir)
    was_created = mc._create_if_not_available(test_fs, zipper_base_path)
    assert not was_created


def test_get_output_path():
    output_path = mc.output_path(test_fs, fs_path, "zapper", 4)
    expected_dir = fs_path + "/zapper/0004/0001"
    assert output_path == expected_dir
    shutil.rmtree(fs_path + "/zapper")


def test_cleanup_generations():
    if not os.path.exists(fs_path + "/zapper"):
        os.mkdir(fs_path + "/zapper")
    test_gens = 10
    for i in range(test_gens):
        p = fs_path + "/zapper/" + mc.common_number_format(i + 1)
        if not os.path.exists(p):
            os.mkdir(p)
    mc.clean_up_generations(test_fs, fs_path + "/zapper/", test_gens // 2)
    for i in range(test_gens // 2):
        assert not os.path.exists(fs_path + "/zapper/" + mc.common_number_format(i + 1))
    for i in range(test_gens // 2, test_gens):
        assert os.path.isdir(fs_path + "/zapper/" + mc.common_number_format(i + 1))
    shutil.rmtree(fs_path + "/zapper")
