class Moteur:
    def __init__(self, puissance) -> None:
        self.puissance = puissance
    
    def demarer (self): pass

class Moteur_Essence(Moteur):
    pass

class Moteur_Electrique(Moteur):
    pass
