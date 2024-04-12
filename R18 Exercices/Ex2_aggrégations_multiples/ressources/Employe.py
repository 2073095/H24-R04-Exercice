class Employe: 
    def __init__(self, id_employe:int, nom:str, prenom:str, role:int, salaire:int) -> None:
        self.id_employe = id_employe
        self.nom = nom
        self.prenom = prenom
        self.role = role
        self.salaire = salaire


class Programmeur(Employe):
    def __init__(self, id_employe: int, nom: str, prenom: str, role: int, salaire: int, _languages:list(str)) -> None:
        super().__init__(id_employe, nom, prenom, role, salaire)
        self._languages = _languages
        

    @property
    def languages_connu(self):
        return self._languages

    @languages_connu.setter
    def ajouter_languages(self, new_language):
        self._languages.append(new_language)

class Designer(Employe):
    def __init__(self, id_employe: int, nom: str, prenom: str, role: int, salaire: int, liste_artefacts:list(str)) -> None:
        super().__init__(id_employe, nom, prenom, role, salaire)
        self.liste_artefacts = liste_artefacts

    def dessiner(self): pass


class Tech_Reseau(Employe):
    def __init__(self, id_employe: int, nom: str, prenom: str, role: int, salaire: int, liste_interventions:list(str)) -> None:
        super().__init__(id_employe, nom, prenom, role, salaire)
        self.liste_interventions = liste_interventions
    
    def intervenir(self): pass

