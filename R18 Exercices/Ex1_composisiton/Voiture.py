from Reservoir import *
from Moteur import *
class Voiture :
    def __init__(self, pPrix:int, pMoteur, pReservoir:int) -> None:
        self.prix = pPrix
        if type(pMoteur) == int :# est un int :
            self.moteur = Moteur(pMoteur)
        else :
            self.moteur = pMoteur
            
        self.reservoir = Reservoir(pReservoir)