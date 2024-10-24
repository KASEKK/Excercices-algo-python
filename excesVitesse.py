#!/bin/python3
vitesseVehicule = int(input("A quelle vitesse rouliez-vous ? "))
vitesseAutorisee = int(input("Quelle était la vitesse autorisée ? "))
excesVitesse = int(vitesseVehicule - vitesseAutorisee)

#Modalités d'amende. A modifier si la loi change. 
exces0a30 = 53
exces0a40 = 53
agloExces30 = "Montant : Tribunal entre 80 EUR et 4000 EUR"
autreExces40 = "Montant : Tribunal entre 80 EUR et 4000 EUR"

decheance20a30 = "une déchéance du droit de conduire : 8 jours > 5 ans (possible)"
decheance30 = "une déchéance du droit de conduire : 8 jours > 5 ans (obligatoire)"
decheance30a40 = "une déchéance du droit de conduire : 8 jours > 5 ans (possible)"
decheance40 = "une déchéance du droit de conduire : 8 jours > 5 ans (obligatoire)"

retrait = "un retrait du permis de conduire : possible"

#Calcul des Km/h en trop
euroParKmhAglo = (excesVitesse -10) * 11
euroParKmhAutre = (excesVitesse - 10) * 6

if vitesseAutorisee < vitesseVehicule :
    if vitesseAutorisee > 50:
        print(f"Vous étiez hors aglomérations. Votre excès de vitesse était de : {excesVitesse} Km/h")
        if excesVitesse <= 10:
            print(f"Le montant de votre amende sera de {exces0a30} EUR")
        elif excesVitesse <= 30:
            print(f"Le montant de votre amende sera de {exces0a30 + euroParKmhAutre} EUR")
        elif excesVitesse <= 40:
            print(f"Le montant de votre amende sera de {exces0a40 + euroParKmhAutre} EUR, {decheance30a40} et {retrait}")
        else:
            print(f"Vous rouliez a plus que 40km/h. Dans ce cas voici ce que la loi prévoit : {autreExces40}, {decheance40}, {retrait}")

    else:
        print(f"Vous étiez dans une zone d'aglomération. Votre excès de vitesse était de {excesVitesse} Km/h")
        if excesVitesse <= 10:
            print(f"Le montant de votre amende sera de {exces0a30} EUR")
        elif excesVitesse <= 20:
            print(f"Le montant de votre amende sera de {exces0a30 + euroParKmhAglo} EUR")
        elif excesVitesse <= 30:
            print(f"Le montant de votre amende sera de {exces0a30 + euroParKmhAglo} EUR et {decheance20a30} et {retrait}")
        else:
            print("Vous aviez un excès de vitesse de plus de 30km/h. Dans ce cas voici ce que la loi prévoit :", agloExces30,",", decheance30a40,",", retrait)
else:
    print("Félicitations, vous rouliez à la vitesse autorisée.")






