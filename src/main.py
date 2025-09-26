import os
import json
import shutil

from utils.download_utils import get_downloads

USER_DIR = os.path.expanduser("~")
DOWNLOAD_DIR = os.path.join(USER_DIR, "Downloads")


def get_structure() -> dict:
    """Finds the desired structure from the config file, if the config file cannot be found asks the user to set a desired path to save into

    :return: dictionary of config file paths
    """
    if not os.path.exists(".dir"):
        json_input = {}
        while True:
            json_input["directory"] = input(
                "enter the desired directory to copy files into: "
            )
            if not os.path.exists(json_input["directory"]):
                print("not a valid directory, try again")
                continue
            break
        with open(".dir", "w+") as file:
            json.dump(json_input, file)
        return json_input
    else:
        with open(".dir", "r") as file:
            return json.loads(file.read())


def main():
    config = get_structure()
    for file in get_downloads():
        shutil.copy(f"{DOWNLOAD_DIR}/{file}", config["directory"])


if __name__ == "__main__":
    main()
