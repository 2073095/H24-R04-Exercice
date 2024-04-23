#TP2 par ........
#
from abc import ABC,abstractmethod
import subprocess as sb

#from .......users.2073095.github-classroom.420-2n6r.tp2-sommatif-individuel-2073095.ressources.AdresseIP import AdresseIP
#from .......users.2073095.github-classroom.420-2n6r.tp2-sommatif-individuel-2073095.ressources.AdresseIP import AdresseIP

#from ressources.AdresseIP import AdresseIP
if __name__ == '__main__' : from AdresseIP import *
else :                      from .AdresseIP import *
#from AdresseIP import *
class Composante(ABC):
    def __init__(self, nom, adresse_ip:AdresseIP, adresse_passerelle:AdresseIP, masque_sous_reseau:AdresseIP, location_physique:str) -> None:
        self._nom = nom
        self._adresse_ip = adresse_ip
        self._adresse_passerelle = adresse_passerelle
        self._masque_sous_reseau = masque_sous_reseau
        self.location_physique = location_physique


#|-----------PROPERTIES ET SETTERS-----------|

    @property
    def nom(self): return self._nom

    @property
    def adresse_ip(self): return self._adresse_ip

    @property
    def adresse_passerelle(self): return self._adresse_passerelle

    @property
    def masque_sous_reseau(self): return self._masque_sous_reseau

    @adresse_ip.setter
    def adresse_ip(self, nouvelle_adresse_ip): self._adresse_ip = AdresseIP(nouvelle_adresse_ip)
    
    @adresse_passerelle.setter
    def adresse_passerelle(self, nouvelle_adresse_passerelle): self._adresse_passerelle = AdresseIP(nouvelle_adresse_passerelle)
    
    @masque_sous_reseau.setter
    def masque_sous_reseau(self, nouveau_masque_sous_reseau): self._masque_sous_reseau = AdresseIP(nouveau_masque_sous_reseau)
    
#|--------------------------------------------|


    def ping(self): 
        try: 
            sb.check_output( ['ping', '-n', '1', str(self.adresse_ip.valeur)], stderr=sb.STDOUT )
            return True
        except sb.CalledProcessError: 
            return False

    @abstractmethod
    def fermer(self): pass


class Poste(Composante):
    def __init__(self, nom, adresse_ip: str, adresse_passerelle: str, masque_sous_reseau: str, location_physique: str) -> None:
        super().__init__(nom, adresse_ip, adresse_passerelle, masque_sous_reseau, location_physique)
        self.est_allume = False
        
    def ouvrir(self):
        # assumez qu'on envoie un signal de s'allumer.... à implanter une autre session.
        if self.est_allume : print("Station déjà ouvert.")
        self.est_allume = True
        
    def fermer(self):
        # assumez qu'on envoie un signal de se fermer.... à implanter une autre session.
        if self.est_allume == False: print ("Station déjà éteinte.")
        self.est_allume = False

class Routeur(Composante):
    def __init__(self, nom, adresse_ip: AdresseIP, adresse_passerelle: AdresseIP, masque_sous_reseau: AdresseIP, location_physique: str, nb_ports:int, ls_connexions:list[Composante]) -> None:
        super().__init__(nom, adresse_ip, adresse_passerelle, masque_sous_reseau, location_physique)
        self._nb_ports = nb_ports
        self._ls_connexions = ls_connexions


    @property
    def nb_ports(self): return self._nb_ports

    @property
    def ls_connexions(self): return self._ls_connexions


# A FAIR POUR LA FIN
    def ajouter_connexion(self, connexion: Composante): 
        if self._nb_ports > len(self._ls_connexions) and connexion not in self._ls_connexions:
            self._ls_connexions.append(connexion)
        #if isinstance(connexion, Routeur) == True:
        #    pass

    def supprimer_connexion(self, connexion: Composante):
        self._ls_connexions.remove(connexion)
    
    def fermer(self):
        print("Cette instruction va fermer le courant vers le routeur.")
        reponse = input("Continuer ? (Y/N)")
        # instructions pour fermer le courant hors du cadre du TP2
    

