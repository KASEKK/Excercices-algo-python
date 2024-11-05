#!/bin/python3
loyer = int(input("Quel est le prix du loyer envisagé ? : "))
salaire = int(input("Quel est le salaire net mensuel ? : "))
if loyer > salaire * 0.4:
    print("Le loyer est trop cher")
else:
    print("Le loyer est abordable")
    