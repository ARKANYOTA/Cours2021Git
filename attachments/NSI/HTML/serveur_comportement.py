# fait en python v3.8

# Depuis le module 'http.server', nous importons le sous modules 'BaseHTTPRequestHandler'
# BaseHTTPRequestHandler : fournis une base pour pouvoir personnaliser le comportement
#                          du serveur, 'BaseHTTPRequestHandler' est fournis de base
#                          avec l'installation de python sur votre machine
from http.server import BaseHTTPRequestHandler

# Depuis le module 'urllib.parse', nous importons le sous module 'urlparse'
# urlparse : permet d'extraire les paramètres de l'URL (utile pour la requête GET !),
#            'urlparse' est fournis de base avec l'installation de python sur votre machine
from urllib.parse import urlparse


# Notre comportement, ou plutot le gestionnaire (handler en anglais) doit être créé à travers une classe
# 'class' est un terme employé dans la Programmation Orientée Objet (POO), thème abordé en terminale
# Si c'est la première fois que vous voyez le terme 'class', dites vous simplement qu'une 'classe' est une variable
# améliorée dans laquelle nous pouvons enregistrer plusieurs données de type different et également des fonctions 
# (qu'on appelle méthode en POO)
# Par convention, le nom d'une classe commence par une lettre majuscule
class Comportement(BaseHTTPRequestHandler): # notre classe 'gestionnaireDuServeur' surcharge les règles définies dans 'BaseHTTPRequestHandler'
    
    # nous devons expliquer comment notre serveur doit réagir si il reçoit une requete
    # de type GET (dans la méthode 'do_GET') ou une requ¼ete de type POST (dans la méthode 'do_POST')

    # Nous expliquons à notre serveur dans cette méthode comment il doit réagir si on le sollicite avec une requête de type 'GET'
    def do_GET(self): 

        # la variable 'urlApresNomDeDomaine' contient tout le chemin après le nom de domaine, quelques exemples de valeurs possibles : 
        # '/'
        # '/?nom=lopez&prenom=matthieu' 
        # '/formulaireGet.html' 
        # '/ressourceinconnue.html'
        urlApresNomDeDomaine = self.path  

        # Le navigateur sollicite automatiquement un favicon, on ignore cette requette pour alléger les logs du 
        # serveur et ainsi les rendre plus facilement lisibles/compréhensibles
        if urlApresNomDeDomaine.endswith('favicon.ico'):
            return

        print("SERVEUR : [GET]")
        print(" - j'ai reçu une requête de type GET de la part du client")

        if urlApresNomDeDomaine == '/formulaireGet.html':
            
            print(" - je construit une réponse et je commence par renseigner les informations d'entête")
            self.send_response(200)                         # on renseigne dans la réponse du serveur le code http 200 pour dire au client que tout s'est bien passé
            self.send_header('Content-type', 'text/html')   # on renseigne dans la réponse du serveur le fait que cette dernière est un texte de type 'html'
            self.end_headers()                              # on cloture la fin du paramétrage de l'entête de la réponse
    
            print(" - Terminé ! maintenant je construis le corps de ma réponse...")
    
            # Notre serveur lit le fichier nommé 'formulaireGet.html', vous devez remplir ce fichier.
            # Il peut contenir du simple code HTML. Ici, pour tester si les requêtes 'GET' fonctionnent bien, vous
            # devez créer une page web contenant un formulaire de type 'GET'
            serverResponseBodyHTML = open('formulaireGet.html').read()
            self.wfile.write(serverResponseBodyHTML.encode("utf-8"))    
            
                
        elif urlApresNomDeDomaine == '/formulairePost.html':
        
            print(" - je construit une réponse et je commence par renseigner les informations d'entête")
            self.send_response(200)                         # on renseigne dans la réponse du serveur le code http 200 pour dire au client que tout s'est bien passé
            self.send_header('Content-type', 'text/html')   # on renseigne dans la réponse du serveur le fait que cette dernière est un texte de type 'html'
            self.end_headers()                              # on cloture la fin du paramétrage de l'entête de la réponse

            print(" - Terminé ! maintenant je construis le corps de ma réponse...")

            # Notre serveur lit dans son dossier un fichier nommé 'formulairePost.html', vous devez créer ce fichier.
            # Il peut contenir du simple code HTML. Ici, pour tester si les requêtes 'POST' fonctionnent bien, vous
            # devez créer une page web contenant un formulaire de type 'POST'        
            serverResponseBodyHTML = open('formulairePost.html').read()
            self.wfile.write(serverResponseBodyHTML.encode("utf-8"))
            
        else:
            
            # 'stringParametresDansURL' contient les paramètres de la requ¼ete GET. Exemple de valeur 'stringParametresRequete' = "nom=lopez&prenom=matthieu"
            stringParametresRequete = urlparse(urlApresNomDeDomaine).query
            
            if stringParametresRequete and urlApresNomDeDomaine.startswith('/reponseGet.html'): # si il y a des parametres dans la requête GET ET si on sollicite la ressource '/reponseGet.html'
                print(" - j'ai trouvé des paramètres GET dans l'url !")
                
                print(" - je construit une réponse et je commence par renseigner les informations d'entête")
                self.send_response(200)                         # on renseigne dans la réponse du serveur le code http 200 pour dire au client que tout s'est bien passé
                self.send_header('Content-type', 'text/html')   # on renseigne dans la réponse du serveur le fait que cette dernière est un texte de type 'html'
                self.end_headers()                              # on cloture la fin du paramétrage de l'entête de la réponse
                
                print(" - Terminé ! maintenant je construis le corps de ma réponse...")
                
                # On capture dans la variable 'dictParametresRequetes' (de type dictionnaire) les paramètres de l'url
                dictParametresRequetes = dict(qc.split("=") for qc in stringParametresRequete.split("&"))
                
                # Puis, en fonction du nombre de parametres, nous créons X lignes de tableau HTML
                champsHTML = ""
                for nomChamp in dictParametresRequetes:
                    champsHTML = champsHTML + f"<tr><td>{nomChamp}</td><td>{dictParametresRequetes[nomChamp]}</td></tr>"
                
                # Nous ajoutons ces lignes dans un body (inutile d'ajouter les balises html, header, body, le 
                # serveur ('BaseHTTPRequestHandler') se charge de les ajouter automatiquement)
                body = """
                <h1>Resultat de la requete GET</h1> 
                <style>
                    table, th, td {
                        border: 1px solid black;
                    }
                    table {border-collapse: collapse;}
                </style>
                <table>
                    <tr>
                        <th>Nom du parametre</th>
                        <th>Valeur du parametre</th> 
                    </tr>
                	""" + champsHTML + """
                </table>
                  """
                
                self.wfile.write(body.encode('utf-8'))
            
            else:
                print(f" - je ne connais pas cette ressource {urlApresNomDeDomaine}")
                print(" - je construit une réponse et je commence par renseigner les informations d'entête. Comme la ressource demandée est inconnu, l'entête de la réponse contiendra le code 404")
                self.send_response(404)                         # on renseigne dans la réponse du serveur le code http 404 pour dire au client que la ressource demandée n'a pas été trouvée
                self.send_header('Content-type', 'text/html')   # on renseigne dans la réponse du serveur le fait que cette dernière est un texte de type 'html'
                self.end_headers()                              # on cloture la fin du paramétrage de l'entête de la réponse
                
                print(" - Terminé ! maintenant je construis le corps de ma réponse...")
                self.wfile.write(f"<h1>Erreur 404 ! page non trouvee ! (la ressource {urlApresNomDeDomaine} m'est inconnue)</h1>".encode('utf-8'))

        print(" - FINI ! j'ai construit la page HTML de mon côté (côté serveur donc) et je l'envoie au client\n\n")

    # Nous expliquons à notre serveur dans cette méthode comment il doit réagir si on le sollicite avec une requête de type 'POST'
    def do_POST(self):

        # la variable 'urlApresNomDeDomaine' contient tout le chemin après le nom de domaine, quelques exemples de valeurs possibles : 
        # '/'
        # '/?nom=lopez&prenom=matthieu' 
        # '/formulaireGet.html' 
        # '/ressourceinconnue.html'
        urlApresNomDeDomaine = self.path          

        if urlApresNomDeDomaine.startswith('/reponsePost.html'): # si on sollicite la ressource '/reponsePost.html'

            # Le serveur vient de recevoir une requête de type 'POST'. Nous capturons dans la variable 'postData' les données 
            # envoyées par le client dans le formulaire 'ressource.html' qu'il a rempli 
            postData = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
    
            print("SERVEUR : [POST]")
            print(" - j'ai reçu une requête de type POST de la part du client")
            print(f" - cette requête POST contient des données de formulaire, ces données sont : \n{postData}\n")
    
            print(" - je construit une réponse et je commence par renseigner les informations d'entête")
            self.send_response(200) # on renseigne dans la réponse du serveur le code http 200 pour dire au client que tout s'est bien passé
            self.send_header('Content-type', 'text/html') # on renseigne dans la réponse du serveur le fait que cette dernière est un texte de type 'html'
            self.end_headers() # on cloture la fin du paramétrage de l'entête de la réponse
            
            print(" - Terminé ! maintenant je construis le corps de ma réponse")
            
            # On capture dans la variable 'dictParametresRequetes' (de type dictionnaire) les paramètres de l'url
            dictParametresRequetes = dict(qc.split("=") for qc in postData.split("&"))
            
            # Puis, en fonction du nombre de parametres, nous créons X lignes de tableau HTML
            champsHTML = ""
            for nomChamp in dictParametresRequetes:
                champsHTML = champsHTML + f"<tr><td>{nomChamp}</td><td>{dictParametresRequetes[nomChamp]}</td></tr>"
                
            # Nous ajoutons ces lignes dans un body (inutile d'ajouter les balises html, header, body, le 
            # serveur ('BaseHTTPRequestHandler') se charge de les ajouter automatiquement)
            body = """
                <h1>Resultat de la requete POST</h1> 
                <style>
                    table, th, td {
                        border: 1px solid black;
                    }
                    table {border-collapse: collapse;}
                </style>
                <table>
                    <tr>
                        <th>Nom du parametre</th>
                        <th>Valeur du parametre</th> 
                    </tr>
                	""" + champsHTML + """
                </table>
                  """
                
            self.wfile.write(body.encode('utf-8'))
            print(" - FINI ! j'ai construit la page HTML de mon côté (côté serveur donc) et je l'envoie au client\n\n")
            
        else:
            print(f" - je ne connais pas cette ressource {urlApresNomDeDomaine}")
            print(" - je construit une réponse et je commence par renseigner les informations d'entête. Comme la ressource demandée est inconnu, l'entête de la réponse contiendra le code 404")
            self.send_response(404)                         # on renseigne dans la réponse du serveur le code http 404 pour dire au client que la ressource demandée n'a pas été trouvée
            self.send_header('Content-type', 'text/html')   # on renseigne dans la réponse du serveur le fait que cette dernière est un texte de type 'html'
            self.end_headers()                              # on cloture la fin du paramétrage de l'entête de la réponse
            
            print(" - Terminé ! maintenant je construis le corps de ma réponse...")
            self.wfile.write(f"<h1>Erreur 404 ! page non trouvee ! (la ressource {urlApresNomDeDomaine} m'est inconnue)</h1>".encode('utf-8'))
            
            
# Attention : vocabulaire POO (Programmation Orientée Objet) dans 3, 2, 1 ...
# la variable 'serveur' est en fait un objet ( = une instanciation d'une classe)
# Un objet peut être vu comme une variable améliorée qui peut contenir des 
# variables de types différents et aussi des fonctions (appelées méthodes ici)
# 'serveur.serve_forever()' signifie donc "prends moi l'objet 'serveur' et utilise
# une de ses méthodes qui est 'server_forever'"
def demarrerLeServeur(serveur):
    serveur.serve_forever()
    
def fermerLeServeur(serveur):
    serveur.server_close()