#JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!

import os
import random
import secrets
import time

def bu(num):
    word = []
    for i in range(num):
        sp = chr(random.randint(0, 130))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))

        word.append(sp)
    return "".join(word)


stes = 15
def seedgen(pasw):
    global stes
    if stes != 15:

        return stes

    stes = 5381
    bpasw = list(pasw)

    for r in range(600000):
        for i in range(len(bpasw)):

            stes = int(((stes * 33) + ord(bpasw[i]) + r) % (2 ** 256))

    return stes


# do not forget iv
def crypto(mes, mode, iv):
    if mode == 1:
        bmes = [ord(c) for c in mes]
        random.seed(seedgen(key) + iv)
        for i in range(len(bmes)):

            try:
                if i > 0:
                    bmes[i] = (bmes[i] + random.randint(100, 100000) - bmes[i - 1] * 10) % 256

                else:
                    bmes[i] = (bmes[i] + random.randint(100, 100000) * iv) % 256

            except:
                print("unexpected error")
                break
    else:
        ivT = mes[:6]
        re = mes[6:]
        bmes = [ord(c) for c in re]
        cbmes = list(bmes)
        random.seed(seedgen(key) + int(ivT))
        for i in range(len(bmes)):

            try:
                if i > 0:
                    bmes[i] = (bmes[i] - random.randint(100, 100000) + cbmes[i - 1] * 10) % 256

                else:
                    bmes[i] = (bmes[i] - random.randint(100, 100000) * int(ivT)) % 256

            except:
                print("invalid password")
                break
    try:
        return bytes(bmes)
    except:
        print("Please try again")


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
        print("Note: The files will be encrypted and the original files will be overwritten.")
        key = input("Please enter a password (or exit): ")
        if key == "exit":
            print("Have a nice day!")
            break
        seedgen(key)

        for i in files:
            with open(i, "rb") as file:
                content = file.read().hex()
                #print(content)
                iv = secrets.randbelow(900000) + 100000


            with open((i), "r+b") as file:

                vers = str(iv).encode('utf-8') + crypto(content, 1, iv)
                #print(vers)

                file.seek(0)
                file.write(vers)
                file.truncate()
                file.flush()
                os.fsync(file.fileno())

            print("File " + i + " has been encrypted.")
        print("All done!")
        print(" ")
        print("Do you want to continue or exit?")
        choice = input("(continue/exit): ").lower()
        if "ex" in choice:
            print("Have a nice day!")
            break
        print(" ")
    stes = 15

    if "dec" in choice:
        f = False
        key = input("Please enter your password (or exit): ")
        if key == "exit":
            print("Have a nice day!")
            break
        seedgen(key)

        for i in files:
            with open(i, "rb")as file:
                vers = file.read()

            vers = vers.decode('latin-1')

            #print(vers)
            try:
                vers = crypto(vers, 2, 0)

            except:
                print("Error: Maybe " + i + " is not encrypted.")
                f = True
                continue

            try:
                test = bytes.fromhex(vers.decode('utf-8'))


            except ValueError:
                print("Error: Maybe wrong password for file " + i)
                f = True
                continue


            with open(i, "wb") as file:
                file.write(test)

            print("File " + i + " has been decrypted.")

        stes = 15
        print("All done!")
        if f == True:
            print("But there were some errors.")
            print(" ")
            f = False