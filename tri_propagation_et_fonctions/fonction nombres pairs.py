#!/bin/python3

def estPair(nombre):
        return nombre % 2 == 0

tabEntiers = [12,4,-8,7,99,14578,32,45,96,-45879,0,45]
# vos instructions ici
i = 0
for nombre in tabEntiers:
  if estPair(nombre):
    i = i+1
print("Le nombre pairs du tableau est de : ", i)
  
# Liste de chaque nombre pair ou impair

for nombre in tabEntiers:
  if estPair(nombre):
    print(nombre, " est pair")
  else:
    print(nombre, " est impair")
