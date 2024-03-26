import random



class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, couleur, prix, etat='neuf'):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.couleur = couleur
        self.prix = prix
        self.etat = etat

    def imprimer_infos(self):
        print(f"{self.__dict__}")
    

class Voiture_electrique(Voiture):
    def __init__(self, marque, modele, annee, kilometrage, couleur, prix, autonomie_max, type_recharge, etat='neuf'):
        super().__init__(marque, modele, annee, kilometrage, couleur, prix, etat)
        self.autonomie_max = autonomie_max
        self.autonomie_actuelle = random.randint(0, self.autonomie_max)
        self.type_recharge = type_recharge


    def recharger(self, temps):
        if self.type_recharge == 'Niveau 2':
            self.autonomie_actuelle += (temps/120)*40
        elif self.type_recharge == 'Rapide(100kw)':
            self.autonomie_actuelle += (temps/8)*40
        elif self.type_recharge == 'Rapide(300kw)':
            self.autonomie_actuelle += (temps/2)*40
        
        if self.autonomie_actuelle >= self.autonomie_max:
            self.autonomie_actuelle = self.autonomie_max
    
auto_paul = Voiture_electrique('Audi', 'Q8', 2021, 10, 'Jaune', '68000$', 400, 'Rapide(100kw)')
auto_Lucie = Voiture_electrique('Chevrolet', 'Silverado', 2023, 10, 'Argent', '86000$', 640, 'Rapide(300kw)')

print(auto_Lucie.autonomie_actuelle)
auto_Lucie.recharger(10)
print(auto_Lucie.autonomie_actuelle)
print(auto_paul.autonomie_actuelle)
auto_paul.recharger(10)
print(auto_paul.autonomie_actuelle)