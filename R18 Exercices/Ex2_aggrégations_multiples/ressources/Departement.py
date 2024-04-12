from .Equipe import Equipe

class Departement:
    def __init__(self, nom:str, equipes:list(Equipe)) -> None:
        self.nom = nom
        self.equipes = equipes

    def ajouter_equipe(self):
        pass