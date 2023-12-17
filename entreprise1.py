

from abc import ABC, abstractmethod

class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite
    
    @property
    def produit(self):
        return self.__produit
    
    @property
    def quantite(self):
        return self.__quantite


class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def code(self):
        return self.__code
    
    @abstractmethod
    def getPrixHT(self):
        pass


class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat
    
    def __str__(self):
        return f"Produit élémentaire - Nom: {self.nom}, Code: {self.code}, PrixAchat: {self.__prixAchat}"
    
    def getPrixHT(self):
        return self.__prixAchat


class ProduitCompose(Produit):
    tauxTVA = 0.18

    def __init__(self, nom, code, fraisFabrication, listeConstituants=None):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = listeConstituants if listeConstituants is not None else []
    
    @property
    def fraisFabrication(self):
        return self.__fraisFabrication
    
    @property
    def listeConstituants(self):
        return self.__listeConstituants
    
    def __str__(self):
        constituant_str = ", ".join([f"{comp.quantite} unité(s) de {comp.produit.nom}" for comp in self.__listeConstituants])
        return f"Produit composé - Nom: {self.nom}, Code: {self.code}, FraisFabrication: {self.__fraisFabrication}, ListeConstituants: {constituant_str}"
    
    def getPrixHT(self):
        prix_ht_total = 0
        for constituant in self.__listeConstituants:
            prix_ht_total += constituant.produit.getPrixHT() * constituant.quantite
        return prix_ht_total + self.__fraisFabrication


# Exemple d'utilisation
p1 = ProduitElementaire("P1", "001", 10.0)
p2 = ProduitElementaire("P2", "002", 15.0)

composition_p3 = [Composition(p1, 2), Composition(p2, 4)]
p3 = ProduitCompose("P3", "003", 5.0, composition_p3)

composition_p4 = [Composition(p2, 3), Composition(p1, 2)]
p4 = ProduitCompose("P4", "004", 7.0, composition_p4)

print(p1)
print(p2)
print(p3)
print(p4)

print("Prix HT P3:", p3.getPrixHT())
print("Prix HT P4:", p4.getPrixHT())

