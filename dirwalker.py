import os, fnmatch, sys, pathlib

def match_name(name, pattern):
    """
    helper function to match a filename
    """
    if fnmatch.fnmatchcase(name, pattern):
        return 1
    else:
        return 0
    

def scan(path):
    """
    general directory scanner
    """
    dirlst = []
    filelst = []
    with os.scandir(path) as i: # scandir returns an iterator
        for j in i:
            if not j.name.startswith('.') and j.is_dir(): # if not a dotfile and is a subdirectory,
                dirlst.append(j.name)
            if not j.name.startswith('.') and j.is_file(): # if not a dotfile and is a normal file,
                filelst.append(j.name)
    
    print("Directories found:")
    for i in dirlst:
        print(i, sep='\n')
    print("Files found:")
    for i in filelst:
        print(i, sep='\n')
    print("\nScan finished\n")

def help():
    """display help"""
    txt = """
    DirWalker - Directory Searcher & Scanner

    Usage:
    1 - Scan a specified directory, or the current directory
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
    return input("Select an option(1-4): ")

def main():
    while True:
        choice = menu().strip()
        if choice == '1':
            scan(os.getcwd())
        elif choice == '2':
            pass
        elif choice == '3':
            help()
        elif choice == '4':
            print("\nExiting...")
            break
        else:
            print("\nInvalid option")

if __name__ == '__main__':
    main()
