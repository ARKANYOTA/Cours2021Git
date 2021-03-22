import os, re
Cours2021GitDirectory = "/home/ay/Documents/Cours2021Git"
os.chdir(Cours2021GitDirectory+"/notes")
a = list(os.listdir())
listoffile=[]
for i in a:
    if bool(re.search("\.md$", i)):
        listoffile +=[i]
print(listoffile)

