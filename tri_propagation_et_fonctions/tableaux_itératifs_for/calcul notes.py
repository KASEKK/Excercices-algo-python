import random
notes = []

for i in range(25):
    note = random.uniform(0, 100)  # Génère un nombre aleatoire entre 0 et 100
    notes.append(note)

# Afficher les notes
print("Notes des étudiants :")
for note in notes:
    print(note)

#boucle pour faire la somme des notes
somme = 0
for note in notes:
    somme += note
    print("La somme des notes est : ", somme)

# Calcul de la moyenne

moyenne = somme / len(notes)

# Affichage de la moyenne
print("La moyenne de la classe est : ",moyenne)
