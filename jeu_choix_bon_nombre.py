#!/bin/python3

nbrUtilisateur = int(input("Rentrer un nombre et découvrez si vous avez gagné ! : "))

while nbrUtilisateur < 1 or nbrUtilisateur > 100:
    print("Le nombre n'est pas bon, retentez encore.")
    nbrUtilisateur = int(input("Rentrer un nombre et découvrez si vous avez gagné ! : "))
else:
    print("Félicitations, vous avez entré un bon nombre.")


