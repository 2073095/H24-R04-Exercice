from Reservoir import *
from Moteur import *
class Voiture :
    def __init__(self, pPrix:int, pMoteur:Moteur, pReservoir:int) -> None:
        self.prix = pPrix
        #self.moteur
        self.reservoir = Reservoir()