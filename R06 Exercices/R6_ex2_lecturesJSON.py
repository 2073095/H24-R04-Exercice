import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Q0 : importez le module json

import json

print(f"Q1{'_'*60}")
# Q1
# Lisez le contenue du fichiers "clients.json"
# Ce fichier contient 3 dictionnaires.
# storer le contenu du fichier lue dans une variable consistant en une liste de dictionnaires
#       utiliser le module json

with open("clients.json", "r", encoding="utf-8") as json_file_reader:
    json_reader = json_file_reader.read()
type(json_reader)

clients = json.loads(json_reader)

print(json.dumps(clients, indent=4))

print(f"Q2{'_'*60}")
# Q2
# passez à travers la liste obtenue à la q1 et imprimer les noms et prénoms de chaque clients

for names in clients:
    print(names['name'])