# Q6
# Ce script sert à corriger des listes de noms ayant des espaces superflus.
# On répète les mêmes lignes de code pour chaque groupe.
# Écrivez une fonction qui permettra d'enlever la duplication de code.
# La structure de la fonction est déjà amorcée.
# L'exécution de votre script devra donner le même résultat que l'exécution du script original
#       c'est-à-dire 3 nouvelles listes de groupes contenant les mêmes noms mais sans espaces superflus.


liste_noms_groupe1 = [" Anna Jacobs","Bertand Dupier ", "Catherine Deschamps", "   William Dupont", "     Loise Vilmar  ", " Toca Lombe"]
liste_noms_groupe2 = [" Mienne Lambert", " Justin Tremblay", " Pok Holmes", "Gertrude Dupé", "Harry Potter   ", "   Garry Smother"]
liste_noms_groupe3 = ["Gard Longe ", " Untel Aknom ", "William Dupont III ", " Steven Stevenson  "]

def correction_espaces_supp(liste:list[str]):
    liste_nom_stripped = []
    for nom in liste:
        nom_corriger = nom.strip()
        liste_nom_stripped.append(nom_corriger)
    return liste_nom_stripped

#print(correction_espaces_supp(liste_noms_groupe1))
#print(correction_espaces_supp(liste_noms_groupe2))
#print(correction_espaces_supp(liste_noms_groupe3))

def correction_liste_nom(liste_noms_groupe1):#selectionne tous, right click, remanier
    liste_groupe1_stripped = []
    for nom in liste_noms_groupe1:
        nom_corriger = nom.strip()
        liste_groupe1_stripped.append(nom_corriger)

correction_liste_nom(liste_noms_groupe1)

#liste_groupe2_stripped = []
#for nom in liste_noms_groupe2:
#    nom_corriger = nom.strip()
#    liste_groupe2_stripped.append(nom_corriger)

#liste_groupe3_stripped = []
#for nom in liste_noms_groupe3:
#    nom_corriger = nom.strip()
#    liste_groupe3_stripped.append(nom_corriger) 


#print(liste_groupe1_stripped)
#print(liste_groupe2_stripped)
#print(liste_groupe3_stripped)