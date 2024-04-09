#-	Les postes de travail ont une propriété ‘utilisation’ qui est une indication pour savoir quels logiciels doivent être installés sur ce poste. Pour cet exercice, nous allons avoir les valeurs : ‘info’, ‘info_réseau’ et ‘info_prog’
#       o	Les logiciels ‘info’ sont installés dans tous les postes de travail.
#       o	Les logiciels ‘info-réseau’ seront installés sur les postes de travail ayant cette utilisation…
#-	Le poste de travail d’un professeur aura tous les logiciels, d’où son utilisation ‘*’.

#-	Vous trouverez ci-joint une liste de logiciels  « logiciels2022_2023.csv » qui comprends les logiciels à  installer sur les postes de travail du département informatique, avec une indication si chaque logiciel est installé pour les 2 voies de sortie du département ou pour une voie de sortie spécifique.
#-	Chacun des postes de travail n’a aucun logiciel d’installés pour le moment.

# Tous les ordniateurs ont le même processeur et la même mémoire vive.
# Certain poste de travail PEUVENT avoir des valeurs différentes de processeur ou de mémoire_vive.
#       un attribut self.processeur est crée uniquement si une valeur autre que None est passé au constructeur.
import csv
import os
os.chdir(os.path.dirname(__file__))

class Ordinateur:
    processeur='Ryzen 3600'
    memoire_vive='16Go'
    def __init__(self,ID, adresseIP) -> None:
        self.ID = ID
        self.adresseIP = adresseIP

    
    def __str__(self) -> str:
        return self.ID
    
    @classmethod
    def upgrader_processeur(cls, nouveau_processeur) -> None:
        cls.processeur = nouveau_processeur
        
    
    @classmethod
    def upgrader_memoire(cls, nouvelle_norme) -> None:
        cls.memoire_vive = nouvelle_norme
    
   
class Poste_de_travail(Ordinateur):
    def __init__(self,ID, adresseIP, utilisation,processeur=None, memoire_vive=None) -> None:
        super().__init__(ID, adresseIP)
        self.liste_logiciels = []
        self.utilisation = utilisation
        self.__charger_logiciels()

        if processeur != None:
            self.processeur = processeur

        elif memoire_vive != None:
            self.memoire_vive = memoire_vive
    
    def __charger_logiciels(self):
        with open("logiciels2022_2023.csv", "r", encoding="utf-8") as csv_reader:
            csv_file_reader = csv.reader(csv_reader, delimiter=';')
            next(csv_reader)
            for donnee in csv_file_reader:
                utils = donnee[2]
                logiciel_version = donnee[0:2]

                if utils == 'info' and self.utilisation == 'info-réseau' or utils == 'info-réseau' and self.utilisation == 'info-réseau':
                    self.liste_logiciels.append(logiciel_version)

                elif utils == 'info' and self.utilisation == 'info-prog' or utils == 'info-prog' and self.utilisation == 'info-prog':
                    self.liste_logiciels.append(logiciel_version)

                elif self.utilisation == '*':
                    self.liste_logiciels.append(logiciel_version)



    # ajoute un str ou list de str à logiciels
    def installer_logiciel(self,logiciel,version) -> None:
        if logiciel and version not in self.liste_logiciels:
            self.liste_logiciels.append(logiciel, version) 
    
    def desinstaller_logiciel(self,logiciel,version) -> None:
        if logiciel and version in self.liste_logiciels:
            self.liste_logiciels.remove(logiciel, version)
    
    def imprimer_liste_logiciels(self) -> None:
        print(self.liste_logiciels)


ordi_prof = Poste_de_travail('LPFINFOPORT001', '192.168.221.21', '*', None, '32Go')
ordi_reseau = Poste_de_travail('LLBINFO060208', '192.168.219.21', 'info-réseau')
ordi_prog = Poste_de_travail('LLBINFO060505', '192.168.220.17', 'info-prog')



print (f"logiciels du prof {len(ordi_prof.liste_logiciels)}")
for logiciels_prof in ordi_prof.liste_logiciels:
    print (f"   {logiciels_prof}")

print (f"Logiciels de réseau {len(ordi_reseau.liste_logiciels)}")
for logiciels_reseau in ordi_reseau.liste_logiciels:
    print (f"   {logiciels_reseau}")

print (f"Logiciels de prog {len(ordi_prog.liste_logiciels)}")
for logiciels_prog in ordi_prog.liste_logiciels:
    print (f"   {logiciels_prog}")