import os

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
        currentDir = directory
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
        os.rmdir(path)
    elif mode == "file":
        try:
            os.remove(path)
        except FileNotFoundError:
            print("File does not exist exists")


#MISC

commandList = ["ls", "pwd", "whoami", "cd", "ls"]
def cmdlist():
    return commandList

def commandCheck():
    if __name__ == "__main__":
        ls()
        pwd()
        whoami()
commandCheck()
rm("./hello.txt", "file")