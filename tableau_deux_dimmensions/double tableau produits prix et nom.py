#!/bin/python3

tableauProduits = (("banane", "pomme", "orange"), (2, 3, 5))

print("Liste des produits et leurs prix :")
for i in range(len(tableauProduits[0])): 
    print("Produit : ", {tableauProduits[0][i]}, "Prix : ", {tableauProduits[1][i]}, " €")


