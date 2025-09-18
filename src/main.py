import os

def main():
    if not os.path.exists(".dir"):
        directory = input("enter the desired directory")
        with open(".dir", "w+") as file:
            file.write(directory)

if __name__ == "__main__":
    main()
