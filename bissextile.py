#!/bin/python3
annee = int(input("Quelle année voulez-vous vérifier ? "))

if annee % 400 == 0:
    print("L'année est bissextile")

if annee % 100 == 0:
    print("L'année n'est pas bissextile")

if annee % 4 == 0:
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")