import Commands

"""V1"""

def checkForCommand(entry):
    if entry == ("l", "s"):
        Commands.ls()
    elif entry[:2] == ("c", "d"):
        path = transformToString(entry[3:])
        Commands.cd(path)
    elif entry == ("w", "h", "o", "a", "m", "i"):
        print(Commands.whoami())
    elif entry[:3] == ("p", "w", "d"):
        print(Commands.pwd())

def transformToString(tuple):
    output = ""
    for x in tuple:
        output += x
    return output

def transfromToTuple(str):
    output = []
    for x in str:
        output.append(x)
    return tuple(output)


#Main Loop NOT TO RUN ON IMPORT
if __name__ == "__main__":
    while True:
        entry = input(Commands.pwd() + " >>>")
        checkForCommand(transfromToTuple(entry))

