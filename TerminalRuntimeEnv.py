import Commands

"""V1"""


def transform_to_string(tuple_entry):
    output = ""
    for x in tuple_entry:
        output += x
    return output


def transform_to_tuple(string):
    output = []
    for x in string:
        output.append(x)
    return tuple(output)


def check_for_command(entry):
    first_space = transform_to_string(entry).find(" ")
    entry_s = transform_to_string(entry)
    print(first_space)


    # if entry == ("l", "s"):
    if entry == transform_to_tuple("ls"):
        Commands.ls()


    # elif entry[:2] == ("c", "d"):
    elif entry[:2] == transform_to_tuple("cd"):
        path = transform_to_string(entry[3:])
        Commands.cd(path)


    # elif entry == ("w", "h", "o", "a", "m", "i"):
    elif entry == transform_to_tuple("whoami"):
        print(Commands.whoami())


    # elif entry == ("p", "w", "d"):
    elif entry == transform_to_tuple("pwd"):
        print(Commands.pwd())


    elif entry_s[:first_space] == "mkdir":
        path = entry_s[first_space+1:]
        Commands.mkdir(path)


    elif entry_s[:first_space] == "rm":
        path = entry_s[first_space+1:]
        try:
            a = open(path, "r")
            mode = "file"
            a.close()
        except:
            mode = "dir"
        Commands.rm(path, mode)


# Main Loop NOT TO RUN ON IMPORT
if __name__ == "__main__":
    while True:
        entry = input(Commands.pwd() + " >>>")
        check_for_command(transform_to_tuple(entry))
