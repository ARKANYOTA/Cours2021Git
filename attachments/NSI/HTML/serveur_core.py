# fait en python v3.8

# Depuis le module 'http.server', nous importons le sous module 'HTTPServer'
# HTTPServer : c'est le coeur du serveur HTTP, 'HTTPServer' est fournis de base
#              avec l'installation de python sur votre machine 
from http.server import HTTPServer

# Depuis le module 'serveur_comportement', nous importons le sous module 'Comportement'
# Comportement : ce sous module est un fichier que j'ai entierement créé et rempli
#                afin de configurer les comportements que doit avoir le serveur
from serveur_comportement import Comportement, demarrerLeServeur, fermerLeServeur

# Dans 'adresseDuServeur', nous saisissons un tuple pour configurer : 
# - le nom de domaine du serveur qui est 'localhost'
# - le port qui est 80 (port utilisé par défault quand on utilise le protocole HTTP)
adresseDuServeur = ('localhost', 80)

# Nous créons notre serveur grâce au constructeur 'HTTPServer' (on parle de constructeur car HTTPServer a éte codé via le paradygme de Programmation Orientée Objet).
# Pour 'construire' notre serveur, nous avons besoin de renseigner les paramètres suivants à notre constructeur 'HTTPServer'
# - l'adresse du serveur, via la variable 'adresseDuServeur'
# - la manière dont doit se comporter notre constructeur, via 'Comportement' qui est définie dans le fichier 'serveur_comportement'
serveur = HTTPServer(adresseDuServeur,Comportement)


# Ensuite nous démarrons notre serveur qui tournera 'pour toujours' tant qu'on ne décide pas de le stopper
print("serveur : je démarre, je me met à l'écoute d'éventuelles requêtes !")
try: # SI l'utilisateur stoppe le serveur via son IDE ou via la ligne de commande une erreur 'KeyboardInterrupt' apparait et le programme s'arrête 
    demarrerLeServeur(serveur)
except KeyboardInterrupt: # SI l'erreur 'KeyboardInterrupt' apparait : 
    pass # ALORS tu ignores l'erreur et tu exécutes les lignes ci-dessous

# Si jamais nous stoppons 'serveur_core.py', nous cloturons proprement le serveur
fermerLeServeur(serveur)
print('Serveur proprement cloturé !')