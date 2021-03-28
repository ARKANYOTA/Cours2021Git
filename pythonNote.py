import os, re
from Get import getkey
# Cours2021GitDirectory = "/home/ay/Documents/Cours2021Git"
os.chdir(os.getcwd()+"\\notes")
liste_dossier = list(os.listdir())
liste_fichier = []
for i in liste_dossier:
    if bool(re.search("\.md$", i)):
        liste_fichier +=[i]


# filename: [tags, created, modified]
info = {}

for file_name in liste_fichier:
    dico_file = []
    # dico_file = {}
    with open(file_name, "r", encoding="utf8") as f:
        f.readline()
        Boucle = True
        while Boucle:
            ligne = f.readline().strip()
            if "---" in ligne:
                Boucle = False
                break
            # ligne = ligne.split(":", 1)
            dico_file += [ligne]
            # dico_file[ligne[0]] = ligne[1]
    info[file_name] = dico_file

for cle,val in info.items():
    print(cle, val)

while True:
    print("\033[2J\033[1;1H--------------------------------")
    for i in range(min(os.get_terminal_size()[1]-2, len(info.keys()))):
        print(list(info.keys())[i])
    if input()=="e":
        exit()

#     print(list(val.keys()))
#while key!="\x03":
#    key = getkey()
#    if key=="\x1b[B":
#        index = (index+1)%number_of_files
#    if key=="\x1b[A":
#        index = (index-1)%number_of_files
#    if key=="\x1b[C":
#        print("right")
#    if key=="\x1b[D":
#        print("left")
#    # print(repr(key))
#    print("----------------------------------") 
#    print("\033[2J\033[1;1H")
#    for i in range(min(number_of_files, os.get_terminal_size()[1]-2)):
#        print("\033["+str(i)+";"+str(5)+"H"+listoffile[i])



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
