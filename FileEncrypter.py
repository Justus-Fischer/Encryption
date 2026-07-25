import json
import os



currentpath= os.path.dirname(os.path.abspath(__file__))


allentries = os.listdir(currentpath)


files = [i for i in allentries if os.path.isfile(os.path.join(currentpath, i))]

print(" ")
print(files)
print(" ")
print(allentries)
print(" ")
print(currentpath)