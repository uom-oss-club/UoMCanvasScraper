import os
import json
import shutil
import inquirer


def get_structure():
    if not os.path.exists(".dir"):
        json_input = {"directory": ""}
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


def get_downloads():
    questions = [
        inquirer.Checkbox(
            "interests",
            message="What are you interested in?",
            choices=[
                file
                for file in os.listdir(f"{os.path.expanduser('~')}/Downloads")
                if file.endswith(".pdf")
            ],
        )
    ]
    answers = inquirer.prompt(questions)


def main():
    config = get_structure()
    in_dir = get_downloads()


if __name__ == "__main__":
    main()
