chiffreAffaire = 0
nombreClients = 0

#tableau de produits et prix (est ce que je ne peux pas faire directement un dictionnaire ?)
nomsProduits = ["banane", "pomme", "orange", "abricot", "avocat", "ananas", "kiwi", "melon", "citron", "peche"]
prixProduits = [1,2,1,2,2,4,2,5,1,2]

finJournee = True

#fontion paiement
def paiement(total):
    paiement = int(input("Le total est de " + str(total) + " euros. Quel montant donnez-vous pour régler ? "))
    restant = total - paiement
    while restant > 0:
        newPaiement = int(input("Il vous reste " + str(restant) + " euros à payer. Quel montant donnez-vous pour régler ? "))
        restant = total - newPaiement - paiement
        paiement = newPaiement + paiement
    if restant == 0:
        print("Le compte est bon, bonne journée. ")
    else: 
        print("Je dois vous rendre " + str(-restant) + " euros. et le compte est bon. Bonne journée. ")
    return total


#fonction ticket
def ticket(tabPrix, tabProd):
    total = 0
    ceSeraTout = True

    while ceSeraTout:
        ref = int(input("Quelle est la référence de votre produit ? "))
        while ref <1 or ref>10:
            ref = int(input("Votre référence n'est pas bonne, retentez encore ! : "))
        print("Vous avez choisi le produit ", tabProd[ref-1],"au prix de ", tabPrix[ref-1], "euros. ")
        reponse = input("Confirmez-vous votre produit ? oui/non : ")
        if reponse == "oui":
            total += tabPrix[ref-1]
        else : print("Le produit est annulé. ")

        print("Voici votre total :", total, "euros. ")
        reponse = input("Ce sera tout ? oui/non : ")
        if reponse == "oui":
            ceSeraTout = False
    return paiement(total)


while finJournee:
    nombreClients += 1
    chiffreAffaire = chiffreAffaire + ticket(prixProduits, nomsProduits)
    reponse = input("Est-ce la fin de journée ? oui/non : ")
    if reponse == "oui":
        finJournee = False
print("Le nombre de clients est de", nombreClients)
print("et le chiffre d'affaire est de", chiffreAffaire, "euros.")
