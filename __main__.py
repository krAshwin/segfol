import sys
from folder_organizer import os, operations, organize
def main():
    organize(sys.argv[1]) #takes the command line argument as input to script

if __name__ == '__main__' : 
    main()
