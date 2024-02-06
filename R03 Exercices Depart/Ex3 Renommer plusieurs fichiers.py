# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

import os

chemain = os.chdir('D:\Session 8\Programmation 2\R03\R03 Exercices Depart\Ex3 Videos')


for video in os.listdir(chemain):
    filename, extension = os.path.splitext(video)
    titre, cours, num = filename.split('_')
    titre = titre.strip()
    num = num.strip().zfill(2)
    nouveau_nom = f'{titre}_{cours}_{num}{extension}'
    os.rename(os.path.join(chemain, filename), os.path.join(chemain, nouveau_nom))