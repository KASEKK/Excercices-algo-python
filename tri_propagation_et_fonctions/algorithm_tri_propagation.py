#!/bin/python3

tailleTableau = int(input("Quelle est la taille du tableau que vous voulez trier ? "))

import random

tabE = [0]*tailleTableau

for i in range(tailleTableau):
  tabE[i] = random.randint(0,10)
print(tabE)

def triTabE(tableauATrier):
   modif = True
   while modif:
      modif = False
      i = 0
      while i < len(tableauATrier)-1:
         if tableauATrier[i] > tableauATrier[i+1]:
            temp = tableauATrier[i]
            tableauATrier[i] = tableauATrier[i+1]
            tableauATrier[i+1] = temp
            modif = True
         i += 1

triTabE(tabE)
print(tabE)