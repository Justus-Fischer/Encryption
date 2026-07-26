#JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!

import os
import random
import secrets


def bu(num):
    word = []
    for i in range(num):
        sp = chr(random.randint(0, 130))
        while not sp.isprintable():
            sp = chr(random.randint(0, 130))

        word.append(sp)
    return "".join(word)


def zkv(wert):
    wert = wert % 0x110000
    if 0xD800 <= wert <= 0xDFFF:
        wert = wert + 2048
    return wert


def zke(wert):
    wert = wert % 0x110000
    if 0xD800 <= wert <= 0xDFFF:
        wert = wert - 2048
    return wert % 0x110000


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
        bmes = list(mes)
        random.seed(seedgen(key) + iv)
        for i in range(len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                if i > 0:
                    bmes[i] = chr(zkv(bmes[i] + random.randint(100, 100000) - ord(bmes[i - 1]) * 10))

                else:
                    bmes[i] = chr(zkv(bmes[i] + random.randint(100, 100000) * iv))

            except:
                print("unexpected error")
                break
    else:
        ivT = mes[:6]
        re = mes[6:]
        bmes = list(re)
        cbmes = list(re)
        random.seed(seedgen(key) + int(ivT))
        for i in range(len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                if i > 0:
                    bmes[i] = chr(zke(bmes[i] - random.randint(100, 100000) + ord(cbmes[i - 1]) * 10))

                else:
                    bmes[i] = chr(zke(bmes[i] - random.randint(100, 100000) * int(ivT)))

            except:
                print("invalid password")
                break
    try:
        return "".join(bmes)
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
                iv = secrets.randbelow(900000) + 100000

            with open(i, "wb") as file:
                vers = str(iv) + crypto(content, 1, iv)
                file.write(vers.encode('utf-8'))

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
        key = input("Please enter your password (or exit): ")
        if key == "exit":
            print("Have a nice day!")
            break
        seedgen(key)

        for i in files:
            with open(i, "rb") as file:
                content = file.read().decode('utf-8')

            with open(i, "wb") as file:
                vers = crypto(content, 2, 0)
                file.write(bytes.fromhex(vers))
            print("File " + i + " has been decrypted.")
        print("All done!")