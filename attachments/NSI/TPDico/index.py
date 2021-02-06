from random import randint
def creer_jeu(fich):
    f=open(fich, "r")
    ligne=f.readline()
    ligne=f.readline()
    dico={}
    while ligne!="":
        L=ligne[:-1].split(";")
        dico[L[0]]=(int(L[1]),int(L[2]))
        ligne=f.readline()
    f.close()
    return dico

def creer_jetons(dico):
    j=[]
    for keys,values in dico.items():
        j+=[keys]*values[1]
    return j

def lire_nom(n):
    print("Nom du joueur n°", n,": ", end="")
    return input()
def init_score(n):
    """n>0"""
    dico={}
    for i in range(0,n):
        dico[lire_nom(i)]=0
    return dico

def maj_score(dico, nom, pt):
    dico[nom]=pt
    return dico

def cpt_pts(dico, mot):
    points = 0
    for i in mot:
        points += dico[i][0]
    return points

def melange(L):
    n=len(L)
    for k in range(n-2):
        rang=randint(k, n-1)
        L[k], L[rang]=L[rang], L[k]
    return L

def Attribution_jetons(score, LesJetons):
    # Donner les jeutons au joureus
    PlayerJetons = {}
    for player in score.keys():
        PlayerJetons[player] = LesJetons[:7]
        LesJetons = LesJetons[7:]
    return (PlayerJetons, LesJetons)
nb_players = int(input("Nombres de Joueurs: "))
score = init_score(nb_players)
langue={
    "A":"scrabblefr.txt",
    "B":"scrabbleuk.txt",
    "C":"scrabbleall.txt",
    "D":"scrabbleesp.txt",
    "E":"scrabbleit.txt",
        }

Langage = input("Quel langues Voulez vous A=FR, B=UK, C=ALL, D=Esp, E=IT: ")

jeu = creer_jeu(langue[Langage])
LesJetons = creer_jetons(jeu)
LesJetons = melange(LesJetons)

PlayerJetons, LesJetons = Attribution_jetons(score, LesJetons)
print(LesJetons)
print(PlayerJetons)

while True:
    for name, points in score.items():
        print("Nom:"+name+", Score:"+str(points)+", Lettres:"+str(PlayerJetons[name]))
        input("pause")
    
