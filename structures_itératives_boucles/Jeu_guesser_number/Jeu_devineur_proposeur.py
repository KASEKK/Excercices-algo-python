#!/bin/python3
"""Le principe global du jeu : 2 joueurs doivent se faire deviner un nombre secret. 
Chacun a 3 tentatives par manche pour deviner le chiffre de l'autre. 
Le premier qui gagne le nombre choisi de manches gagnantes a gagné. 
Chaque joueur est à la fois devineur et proposeur à chaque manche.

Donc, à chaque manche il y en a un qui insère un chiffre et puis l'autre doit deviner, 
ensuite à la deuxième partie de la manche, c'est l'inverse. (il y a un risque d'égalité donc)"""


nomJoueur1 = input("Joueur 1 indiquez votre prénom : ")
nomJoueur2 = input("Joueur 2 indiquez votre prénom : ")

nbrProposeur = 0
nbrDevineur = 0

victoires1 = 0
victoires2 = 0

tentatives = 0

manchesGagnantes = int(input("En combien de manches gagnantes la partie sera gagnée ? "))


for i in range(manchesGagnantes):

# Joueur 1 (proposeur) propose un nombre secret
    nbrProposeur = int(input(nomJoueur1 + " rentrez un nombre secret entre 1 et 100 : "))

    while nbrProposeur < 1 or nbrProposeur > 100:
      nbrProposeur = int(input("Le nombre n'est pas entre 1 et 100, retentez encore ! "))
    
    tentatives = 1
    print("C'est votre tentative : ", tentatives)
    nbrDevineur = int(input(nomJoueur2 + " essayez de deviner le numéro entre 1 et 100 : "))

# Joueur 2 (devineur) tente de deviner le nombre secret en 3 tentatives
    while (nbrDevineur < nbrProposeur or nbrDevineur > nbrProposeur) and tentatives < 3:
      tentatives = tentatives + 1
      if nbrDevineur > nbrProposeur:
          print("C'est votre tentative : ", tentatives)
          nbrDevineur = int(input("Votre nombre est plus grand que celui que vous devez deviner. Retentez encore ! : "))
    

      else:
        print("C'est votre tentative : ", tentatives)
        nbrDevineur = int(input("Votre nombre est plus petit que celui que vous devez deviner. Retentez encore ! : "))
        
# Affichage résultat  du joueur 2 (devineur)        
    if nbrDevineur == nbrProposeur:
        print(nomJoueur2, " vous avez gagné votre partie de la manche ", i+1)
        victoires2 = victoires2 + 1
    else:
        print(nomJoueur2, " vous avez perdu votre partie de la manche ", i+1)
        victoires1 = victoires1 + 1

# Seconde partie de la manche (inversée) : 
# joueur 2 (proposeur) propose un nombre secret 
# et joueur 1 (devineur) tente de le deviner en 3 tentatives
    nbrProposeur = int(input(nomJoueur2 + " rentrez un nombre secret entre 1 et 100 : "))
    while nbrProposeur < 1 or nbrProposeur > 100:
      nbrProposeur = int(input("Le nombre n'est pas entre 1 et 100, retentez encore ! "))

    tentatives = 1
    print("C'est votre tentative : ", tentatives)
    nbrDevineur = int(input(nomJoueur1 + " essayez de deviner le numéro entre 1 et 100 : "))

# Joueur 1 tente de deviner avec 3 tentatives           
    while (nbrDevineur < nbrProposeur or nbrDevineur > nbrProposeur) and tentatives < 3:
      tentatives = tentatives + 1
      if nbrDevineur > nbrProposeur:
         print("C'est votre tentative : ", tentatives)
         nbrDevineur = int(input("Votre nombre est plus grand que celui que vous devez deviner. Retentez encore ! : "))

      else:
        print("C'est votre tentative : ", tentatives)
        nbrDevineur = int(input("Votre nombre est plus petit que celui que vous devez deviner. Retentez encore ! : "))

# Vérification du résultat du joueur 1 (devineur)          
    if nbrDevineur == nbrProposeur:
      print(nomJoueur1, " vous avez gagné votre partie de la manche ", i+1)
      victoires1 = victoires1 + 1
    else:
      print(nomJoueur1, " vous avez perdu votre partie de la manche ", i+1)
      victoires2 = victoires2 + 1

# Affichage du gagnant de la partie      
if victoires1 > victoires2:
  print("Le gagnant est ", nomJoueur1)
elif victoires1 == victoires2:
  print("C'est une égalité !")
else:
  print("Le gagnant est ", nomJoueur2)

