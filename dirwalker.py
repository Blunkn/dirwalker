# all of these libraries are native
import os, fnmatch, sys, pathlib

def match_name(name, pattern):
    """
    helper function to match a filename; CASE SENSITIVE

    args:
    name - name of the file to look up
    pattern - unix style pattern to match against

    returns:
    bool on whether it matches
    """
    if fnmatch.fnmatchcase(name, pattern):
        return True
    else:
        return False
    

def scan(fpath):
    """
    general directory scanner

    args:
    fpath - directory path to look into; uses working directory as default if not specified

    returns:
    N/A
    it just prints stuff lol
    """
    for root, dirnames, fnames in os.walk(fpath, topdown=True):
        print(f"Directories found in {root}:")
        if len(os.listdir(root)) == 0 or len(fnames) == 0:
            print("Directory is empty")
        else:
            print(dirnames)
            print(f"Files found in {root}:")
            print(fnames)

def search(name):
    """
    file searcher for the current directory & subdirectories

    args:
    name - string for a specific input file name; exits to menu if not specified

    returns:
    N/A
    it also just prints stuff
    """
    found = False
    for root, dirnames, fnames in os.walk(os.getcwd(), topdown=True):
        if name in str(fnames):
            print(f"\nFile found in {root}, under {dirnames}")
            found = True
        else:
            continue

    if found == False:
        print("Not found")

def help():
    """display help"""
    txt = """
    DirWalker - Directory Searcher & Scanner
    Version 0.2.0

    Usage:
    1 - Scan a specified directory; script scans everything in current directory by default
    2 - Search for files in a specified directory, or the current directory
    3 - Print help
    4 - Exit
    """
    print(txt)

def menu():
    print("\nDirWalker")
    print("Please choose an option:")
    print("1 - Scan directory")
    print("2 - Search files")
    print("3 - Help")
    print("4 - Exit")
    return input("Select an option (1 - 4): ")

def main():
    while True:
        choice = menu().strip()
        if choice == '1':
            ans = input("Please input subdirectory to scan: ")
            if len(ans) == 0:
                scan(os.getcwd())
            elif not (fnmatch.fnmatchcase(i, ans) for i in os.listdir(ans)):
                print("Subdirectory not found")
            else:
                scan(ans)
        elif choice == '2':
            ans = input("Please input file name to find: ")
            if len(ans) == 0:
                print("\nInvalid option")
            else:
                search(ans)
        elif choice == '3':
            help()
        elif choice == '4':
            print("\nExiting...")
            break
        else:
            print("\nInvalid option")

if __name__ == '__main__':
    main()
