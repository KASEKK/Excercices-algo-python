#!/bin/python3
loyer = int(input("Loyer : "))
salaire = int(input("Salaire : "))

decision = "Abordable" if loyer*0.4 < salaire else "Inabordable"
print(decision)