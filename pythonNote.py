import os, re
from Get import getkey
Cours2021GitDirectory = "/home/ay/Documents/Cours2021Git"
os.chdir(Cours2021GitDirectory+"/notes")
a = list(os.listdir())
listoffile=[]
for i in a:
    if bool(re.search("\.md$", i)):
        listoffile +=[i]
print(listoffile)


# filename: [tags, created, modified]
infos = {}

key = ""
index = 0
number_of_files = len(listoffile)
while key!="\x03":
    key = getkey()
    if key=="\x1b[B":
        index = (index+1)%number_of_files
    if key=="\x1b[A":
        index = (index-1)%number_of_files
    if key=="\x1b[C":
        print("right")
    if key=="\x1b[D":
        print("left")
    # print(repr(key))
    print("----------------------------------") 
    print("\033[2J\033[1;1H")
    for i in range(min(number_of_files, os.get_terminal_size()[1]-2)):
        print("\033["+str(i)+";"+str(5)+"H"+listoffile[i])

"""
info = {}
for i in listoffile:
    with open(i, "r") as f:
        f.readline()
        sl = {}
        sl["tags"] = f.readline().replace('\n', "")
        f.readline()
        sl["created"] = f.readline().replace('\n', "")
        sl["modified"] = f.readline().replace('\n', "")
        info[i] = sl

for i in info.items():
    print(i)

"""
