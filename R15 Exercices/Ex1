class Personne:
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance


class Joueur(Personne):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position):
        super().__init__(nom, prenom, date_naissance)
        self.no_chandail = no_chandail
        self.position = position


class Attaquant(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_tirs_au_but, nb_assistance):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_tirs_au_but = nb_tirs_au_but
        self.nb_assistance = nb_assistance

    def compter_but(self):
        self.nb_tirs_au_but += 1


class Defenseur(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_interceptions, nb_passes):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_interceptions = nb_interceptions
        self.nb_passes = nb_passes


class Gardien(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_arrets, nb_tirs_essuyes):
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_arrets = nb_arrets
        self.nb_tirs_essuyes = nb_tirs_essuyes
    
    def arreter_tir(self):
        self.nb_arrets += 1


class Equipe:
    nbr_joueurs_dans_ligue = 0
    def __init__(self, nom, liste_joueurs:list = []):
        self.nom = nom
        self.liste_joueurs = liste_joueurs
        Equipe.nbr_joueurs_dans_ligue = len(liste_joueurs)

    def engager_joueur(self, joueur):
        self.liste_joueurs.append(joueur)
        Equipe.nbr_joueurs_dans_ligue += 1
        
    
    def ejecter_joueur(self, joueur):
        self.liste_joueurs.remove(joueur)
        Equipe.nbr_joueurs_dans_ligue -= 1
        


gardien_Logan_Ketterer = Gardien('Ketterer', 'Logan', '9 novembre 1993', 1, 'Guardien', 128, 208)
defenseur_Zachary_Brault_Guillard = Defenseur('Brault-Guillard', 'Zachary', '5 mars 1991', 15, 'défenseur gauche', 32, 44)
attaquant_Sunsi_Ibrahim = Attaquant('Ibrahim', 'Sunsi', '1 octobre 2002', 14, 'centre', 23, 44)

equipe_CF_Montreal = Equipe('CF Montréal')

equipe_CF_Montreal.engager_joueur([gardien_Logan_Ketterer])
equipe_CF_Montreal.engager_joueur([defenseur_Zachary_Brault_Guillard])
equipe_CF_Montreal.engager_joueur([attaquant_Sunsi_Ibrahim])

equipe_CF_Montreal.ejecter_joueur([defenseur_Zachary_Brault_Guillard])

print()