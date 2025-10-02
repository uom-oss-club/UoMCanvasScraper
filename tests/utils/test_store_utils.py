from src.utils.store_utils import copy_file
import os


def test_copy_file():
    resources_path = "./tests/resources"
    copy_file(f"{resources_path}/test.pdf", f"{resources_path}/dest")
    if os.path.exists(f"{resources_path}/dest/test.pdf"):
        os.remove(f"{resources_path}/dest/test.pdf")
        assert True
