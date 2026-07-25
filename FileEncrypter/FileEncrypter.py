#JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!

import json
import os

print("JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!")
print("It is possible that data cannot be decrypted")
print("")
print(" ")


while True:

    currentpath = os.path.dirname(os.path.abspath(__file__))

    allentries = os.listdir(currentpath)

    files = [i for i in allentries if os.path.isfile(os.path.join(currentpath, i))]

    print("Welcome to FileEncrypter!")
    print("Currently active in " + currentpath)
    print("")
    print("The FileEncrypter found the following files in the current directory:")
    print("")
    can = 0
    for i in files:
        if i != "FileEncrypter.py":
            print(i)
            can = can + 1
    if can == 0:
        print("No files found.")
        break

    print("")
