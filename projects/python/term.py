import os

def welcome():
    print("                                        *********************")
    print("                                        |  Simple Terminal  |")
    print("                                        *********************")

commands = ("wai", "ls", "mt", "mf", "rf", "md", "rd", "q", "quit")
def display_cmds():
    print("CMDs:-")
    print("-----")
    print("1)wai (Where Am I)")
    print("2)ls (List Dirs)")
    print("3)mt (move to dir)")
    print("5)mf (Make File)")
    print("6)rf (Remove File)")
    print("7)md (Make Dir)")
    print("8)rd (Remove Dir)\n")

def wai():
    print(os.getcwd())

def ls(dir):
    print(os.listdir(dir))

def mt(path):
    os.chdir(path)

def mf(path, name):
    new_file = os.open(f"{path}/{name}", os.O_CREAT | os.O_RDONLY)
    os.close(new_file)

def rf(path, name):
    os.remove(f"{path}/{name}")
    
def md(path, name):
    os.mkdir(f"{path}/{name}")

def rd(path, name):
    os.rmdir(f"{path}/{name}")

class Path:
    def __init__(self, path):
        self.path = path

def check_path(path):
    if os.path.exists(path):
        return True
    else:
        return False

def main():
    welcome()
    display_cmds()
    shelling = True

    while shelling:
        cmd = input(f"$")
        if not cmd in commands:
            print("Command Not Found!")
        else:
            match cmd:
                case "wai":
                    wai()
                case "q" | "quit":
                    print("I'm here if you want to shell again, bye")
                    shelling = False
                case "ls" | "mt" | "mf" | "rf" | "md" | "rd":
                    dir_or_file = Path(input("Enter a path: "))
                    check_path(dir_or_file.path)
                    if check_path(dir_or_file.path) == True:
                        if cmd == "ls":
                            ls(dir_or_file.path)
                        elif cmd == "mt":
                            mt(dir_or_file.path)
                        elif cmd == "mf":
                            mf(dir_or_file.path, input("Enter the file name: "))
                        elif cmd == "rf":
                            rf(dir_or_file.path, input("Enter the file name to be removed: "))
                        elif cmd == "md":
                            md(dir_or_file.path, input("Enter the dir name: "))
                        elif cmd == "rd":
                            rd(dir_or_file.path, input("Enter the dir name to be removed: "))
                    else:
                        print("Dir/File doesn't exist")

if __name__ == "__main__":
    main()
