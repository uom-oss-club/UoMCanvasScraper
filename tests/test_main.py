from src.utils.download_utils import get_files


def test_action():
    assert True


def test_get_downloads():
    assert get_files("./tests/resources") == ["test2.pdf", "test.pdf"]
