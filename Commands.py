import os
import shutil


def ls():
    dirs = os.listdir()
    for obj in dirs:
        print(f"    {obj}")


def pwd():
    return os.getcwd()


def whoami():
    return os.getlogin()


def cd(directory):
    try:
        os.chdir(str(directory))
    except PermissionError:
        print("Access Denied")
    except FileNotFoundError:
        print("Incorrect file directory")


def mkdir(path):
    try:
        os.mkdir(path)
    except FileNotFoundError:
        print("File Already Exists")
    except FileExistsError:
        print("File Already Exists")


def rm(path, mode):
    if mode == "dir":
        shutil.rmtree(path)
    elif mode == "file":
        try:
            os.remove(path)
        except FileNotFoundError:
            print("File does not exist exists")


# MISC

commandList = ["ls", "pwd", "whoami", "cd", "ls"]


def cmd_list():
    return commandList



# commandCheck()
# rm("./hello.txt", "file")
