class Moteur:
    def __init__(self, puissance) -> None:
        self.puissance = puissance
    
    def demarer (self): pass

class Moteur_Essence(Moteur):
    def __init__(self, puissance, nbr_cylindres:int) -> None:
        super().__init__(puissance)
        self.nbr_cylindres = nbr_cylindres
class Moteur_Electrique(Moteur):
    def __init__(self, puissance, emperrage) -> None:
        super().__init__(puissance)
        self.emperrage = emperrage