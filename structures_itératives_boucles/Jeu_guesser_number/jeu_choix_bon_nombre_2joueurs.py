#!/bin/python3

joueur1 = int(input("Joueur 1, rentrez un nombre secret entre 1 et 100 : "))
tentatives = 1

while joueur1 < 1 or joueur1 > 100:
    joueur1 = int(input("Le nombre n'est pas entre 1 et 100. Retentez encore ! : "))
else:
    joueur2 = int(input("Joueur 2, essayez de deviner le numéro entre 1 et 100 du joueur 1 : "))
    while joueur2 < joueur1 or joueur2 > joueur1:
        tentatives = tentatives + 1
        if joueur2 > joueur1:
            joueur2 = int(input("Votre nombre est plus grand que celui du joueur1. Retentez encore ! : "))
        else:
            joueur2 = int(input("Votre nombre est plus petit que celui du joueur1. Retentez encore ! : "))
    else:
        print("Vous avez trouvé le bon nombre en ", tentatives, " fois !")