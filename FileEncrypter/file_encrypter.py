#JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!

import os


print("JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!")
print("It is possible that data cannot be decrypted")
print("")
print("It is recommended to execute this script in a separate folder")
print(" ")
print("Do you want to continue or exit?")
choice = input("(continue/exit): ").lower()

while True:
    if "ex" in choice:
        print("Have a nice day!")
        break

    currentpath = os.path.dirname(os.path.abspath(__file__))

    allentries = os.listdir(currentpath)

    files = [i for i in allentries if os.path.isfile(os.path.join(currentpath, i)) and i != "file_encrypter.py"]

    print("Welcome to the File_Encrypter!")
    print("Currently active in " + currentpath)
    print("")
    print("The FileEncrypter found the following files in the current directory:")
    print("")
    can = 0
    for i in files:

        print(i)
        can = can + 1

    if can == 0:
        print("No files found.")
        break

    print("")
    print("Do you want to encrypt or decrypt these files?")
    choice = input("(Encrypt/Decrypt/Exit): ").lower()
    if "ex" in choice:
        print("Have a nice day!")
        break

    if "enc" in choice:
        print("Note: The files will be encrypted and the original files will be deleted.")
        key = input("Please enter a password (or exit): ")
        if key == "exit":
            print("Have a nice day!")
            break
        for i in files:
            with open(i, "rb") as file:
                content = file.read().hex()
                print(bytes.fromhex(content).decode('utf-8'))

                with open(i, "wb") as file:
                    file.write(bytes.fromhex(content))

