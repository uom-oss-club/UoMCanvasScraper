import os
import inquirer3

USER_DIR = os.path.expanduser("~")
DOWNLOAD_DIR = os.path.join(USER_DIR, "Downloads")


def get_downloads() -> list:
    """gets all pdfs from the downloads directory and asks user to select some

    :return: list of selected pdfs
    """
    questions = [
        inquirer3.Checkbox(
            "interests", message="What are you interested in?", choices=get_files()
        )
    ]
    return inquirer3.prompt(questions)["interests"]


def get_files(dir: str = DOWNLOAD_DIR) -> list:
    """returns a list of files in the given directory

    :param dir: directory to search in
    :return: list of pdfs in directory
    """
    return [file for file in os.listdir(dir) if file.endswith(".pdf")]
