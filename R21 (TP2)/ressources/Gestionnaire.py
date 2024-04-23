#TP2 par Gabriel Boyer

import time
if __name__ == '__main__' : from Composantes import *
else :                      from .Composantes import *


class SousReseau:
    def __init__(self, nom:str, ls_composantes:list[Composante]):
        self._nom = nom
        self._ls_composantes = ls_composantes


    @property
    def nom(self): return self._nom

    @property
    def ls_composantes(self): return self._ls_composantes


    def ping(self):
        try: 
            sb.check_output( ['ping', '-n', '1', str(self.adresse_ip.valeur)], stderr=sb.STDOUT )
            return True
        except sb.CalledProcessError: 
            return False

    def get_composante_par_ip(self, adress_ip_comp:str):
        composante:Composante
        for composante in self._ls_composantes:
            if adress_ip_comp == str(composante.adresse_ip):
                return composante

    def ajouter_composante(self, composante_a_ajouter:Composante):
        if composante_a_ajouter not in self._ls_composantes:
            self._ls_composantes.append(composante_a_ajouter)

    def enlever_composante(self, composante_a_enlever:Composante):
        if composante_a_enlever in self._ls_composantes:
            self._ls_composantes.remove(composante_a_enlever)


class Gestionnaire:
    def __init__(self, nom, reseau:SousReseau):
        self._nom = nom
        self._reseau = reseau

    @property
    def nom(self): return self._nom

    @property
    def reseau(self): return self._reseau
    

    def tester_connexion(self, composante:Composante):
        resultat_composante = composante.ping()
        print(f"Le résultat de la composante est:{resultat_composante}")

    def tester_toutes_connexions(self): 
        for composante_reseau in self._reseau._ls_composantes:
            self.tester_connexion(composante_reseau)

    def redemarrer_station(self, station:Poste):
        station.fermer()
        time.sleep(1)
        station.ouvrir()


if __name__ == "__main__" :
    pass