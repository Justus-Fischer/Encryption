#JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!
import random
import secrets

def fillup(password):
    filledpassword = password.ljust(35,"\x00")
    return filledpassword

def short(password):
    shortpassword = password.rstrip("\x00")
    return shortpassword

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

def seedgen(pasw):

    stes = 5381
    bpasw = list(pasw)
    #pr = time.time()
    for r in range(600000):
        for i in range(len(bpasw)):

            stes = int(((stes * 33) + ord(bpasw[i]) + r) % (2 ** 256))
    #print(time.time()-pr)
    return stes

#do not forget iv
def crypto(mes,mode):
    
    if mode == 1:
        bmes = list(mes) 
        random.seed(seedgen(key)+iv)
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                if i > 0:
                    bmes[i] = chr(zkv(bmes[i] + random.randint(100, 100000) - ord(bmes[i-1])*10))
                    
                else:
                    bmes[i] = chr(zkv(bmes[i] + random.randint(100, 100000)*iv))
                    
            except:
                print("unexpected error")
                break
    else:
        ivT = mes[:6]
        re = geheimtext = mes[6:]
        bmes = list(re)
        cbmes = list(re)
        random.seed(seedgen(key)+int(ivT))
        for i in range (len(bmes)):
            bmes[i] = ord(bmes[i])
            try:
                if i > 0:
                    bmes[i] = chr(zke(bmes[i] - random.randint(100, 100000) + ord(cbmes[i-1])*10))
                    
                else:
                    bmes[i] = chr(zke(bmes[i] - random.randint(100, 100000)*int(ivT)))
                    
            except:
                print("invalid password")
                break
    try:
        return "".join(bmes)
    except:
        print("Please try again")
    
            

    
print("Welcome to the Encryption_Tool!")  
print("JUST A DEMO - DO NOT USE FOR REAL SENSITIVE DATA!")
print(" ")

while True:
    print("Do you want to Encrypt or Decrypt? (En/De)")
    if "EN" in input().upper():
        print('Choose your password or type "generate" for a password which is saver')
        sp = input()
        if "GEN" in sp.upper():
            key = str(bu(random.randint(10, 15))) 
        else:
            key = str(sp)
            
        iv = secrets.randbelow(900000) + 100000
        print("Type in the message that should be encrypted")
        mes = str(input())
        
        print("Your encrypted message is: ")
        print(" ")
        print(str(iv)+str(crypto(fillup(mes),1)))
        print(" ")
        print("Please don't forget your password: " + str(key))
            
        
        
    else:
        print("Type in/Paste the encrypted message")
        mes = str(input())
        print("Type in the password")
        key = str(input())
        print(" ")
        print("The decrypted message is: ")
        print(" ")
        print(str(short(crypto(fillup(mes),2))))
        print(" ")
