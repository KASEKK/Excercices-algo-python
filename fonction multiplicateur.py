#!/bin/python3
def multiplicateurTableau(tableau):
    resultat = 1
    for nombre in tableau:
        resultat *= nombre
    return resultat

tableau = [2, 3, 4, 5]
print("Le produit de tous les nombres du tableau est :", multiplicateurTableau(tableau))