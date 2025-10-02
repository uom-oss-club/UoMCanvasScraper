import shutil


def display_options(files: list[str], store_all: bool = False) -> None:
    """display the options for storing the files

    :param files: files that were selected
    :param store_all: store all the selected files in a directory
    """
    pass


def copy_file(file: str, path: str) -> None:
    """copies the file into the respective directory

    :param file: the file path to be copied
    :param path: the path where it will be copied to
    """
    shutil.copy(file, path)
