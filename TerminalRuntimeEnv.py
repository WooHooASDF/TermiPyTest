import Commands

"""V1"""


def transformToString(tuple):
    output = ""
    for x in tuple:
        output += x
    return output

def transformToTuple(str):
    output = []
    for x in str:
        output.append(x)
    return tuple(output)



def checkForCommand(entry):
    #if entry == ("l", "s"):
    if entry == transformToTuple("ls"):
        Commands.ls()
    #elif entry[:2] == ("c", "d"):
    elif entry[:2] == transformToTuple("cd"):
        path = transformToString(entry[3:])
        Commands.cd(path)
    #elif entry == ("w", "h", "o", "a", "m", "i"):
    elif entry == transformToTuple("whoami"):
        print(Commands.whoami())
    #elif entry == ("p", "w", "d"):
    elif entry == transformToTuple("pwd"):
        print(Commands.pwd())
    #elif entry[:3] == ("m", "k", "d", "i", "r"):
    elif entry[:5] == transformToTuple("mkdir"):
        path = transformToString(entry[6:])
        Commands.mkdir(path)



#Main Loop NOT TO RUN ON IMPORT
if __name__ == "__main__":
    while True:
        entry = input(Commands.pwd() + " >>>")
        checkForCommand(transformToTuple(entry))

