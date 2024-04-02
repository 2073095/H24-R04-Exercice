import random

class Personne:
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
    
class Employe(Personne):
    def __init__(self, nom, prenom, date_naissance, poste, salaire):
        super().__init__(nom, prenom, date_naissance)
        self.NAS = random.randint(1000, 9999)
        self.poste = poste
        self.salaire = salaire

class Realisateur(Employe):
    def __init__(self, nom, prenom, date_naissance, NAS, poste, salaire, bonus):
        super().__init__(nom, prenom, date_naissance, NAS, poste, salaire)
        self.bonus = bonus

class Acteur(Employe):
    def __init__(self, nom, prenom, date_naissance, poste, salaire, role):
        super().__init__(nom, prenom, date_naissance, poste, salaire)
        self.role = role

class Film:
    def __init__(self, nom, date_sortie, liste_employes:list=[]):
        self.nom = nom
        self.liste_employes = liste_employes
        self.date_sortie = date_sortie

film_Titanic = Film('Titanic', '19 décembre 1997')
film_Abyss = Film('Abyss', '9 août 1989')
film_Avatar = Film('Avatar', '18 décembre 2009')

realisateur_James_Cameroun = Realisateur('Cameroune', 'James', '16 août 1954', 1234, 'réalisateur', '2$', 'rien')

print (realisateur_James_Cameroun)