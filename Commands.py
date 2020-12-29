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

def rm(path):
    return

commandList = ["ls", "pwd", "whoami", "cd", "ls"]
def cmdlist():
    return commandList

def commandCheck():
    if __name__ == "__main__":
        ls()
        pwd()
        whoami()
commandCheck()
