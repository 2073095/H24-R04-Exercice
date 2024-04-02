class Département:
    def __init__(self, pId, pNom, pBudget_annuel):
        self.id = pId
        self.nom = pNom
        self.budget_annuel = pBudget_annuel

class Achat:
    def __init__(self, pId, pMontant_total_achat, pEst_paye) -> None:
        self.id = pId
        self.montant_total_achat = pMontant_total_achat
        self.est_paye = pEst_paye
        
    def calculer_total_estime(self):
        pass
    
    def payer(self):
        pass

class Equipement:
    def __init__(self, pId, pNom_equipement, pCle, pModele, pQty, pPrix):
        self.id = pId
        self.nom_equipement = pNom_equipement
        self.cle = pCle
        self.modele = pModele
        self.qty = pQty
        self.prix = pPrix