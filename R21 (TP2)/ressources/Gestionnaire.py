#TP2 par ........

import time
if __name__ == '__main__' : from Composantes import *
else :                      from .Composantes import *


class SousReseau:
    def __init__(self, _nom:str, _ls_composantes:list[Composante]):
        self._nom = _nom
        self._ls_composantes = _ls_composantes


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
        comp:Composante
        for comp in self._ls_composantes:
            if adress_ip_comp == str(comp.adresse_ip):
                return comp

    def ajouter_composante(self): pass

    def enlever_composante(self): pass


class Gestionnaire:
    def __init__(self, nom, _reseau):
        self.nom = nom
        self._reseau = _reseau

    def tester_connexion(self): pass

    def tester_toutes_connexions(self): pass

    def redemarrer_poster(self): pass


if __name__ == "__main__" :
    pass