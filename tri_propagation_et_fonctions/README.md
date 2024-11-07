EXPLICATIONS DE L'ORDINNOGRAMME FLOWGORITHM CONCERNANT LA FONCTION PRINT APPLIQUEE SUR DEUX TABLEAUX DONT LA TAILLE EST DEFINIE PAR L'UTILISATEUR

Etapes : 

- créer une variable tailleTableau qui permet à l'utilisateur de définir la taille du premier tableau

- ensuite on déclare le tableau en tant que tel avec pour taille le contenu de la variable tailleTableau

- on déclare i dont on aura besoin dans la boucle for 

- on crée une boucle for, pourquoi ? Comme ça on crée un compteur qui va parcourir les index du tableau et affecter des valeurs aux éléments du tableau. On décide que ce sera une valeur aléatoire

- détail de la boucle for : la variable i va parcourir tailleTableau de l'indice 0 et augmenter de 1 à chaque boucle jusqu'à ce qu'elle atteigne l'indice de tailleTableau -1

- Ensuite, quand on est sorti de la boucle on va redemander à l'utilisateur de choisir la taille de son deuxième tableau

- Pour ça, on va dupliquer la sortie et l'entrée pour lui demander la taille du tableau, et on va dupliquer la boucle aussi. On ne duplique pas la variable tailleTableau parce qu'utilisée à cet endroit elle est réinitialisée avec une nouvelle valeur. 

- Enfin, on va faire appel à la fonction printE pour afficher le premier et le deuxième tableau



Initialisation de la fonction printE dans flowgorithm : 

- on va gérer la fonction dans une page parallèle et créer printE

- on va lui ajouter un paramètre qui sera un tableau entier nommé tab et qui ne renvoi aucun retour (return) parce que la fonction d'affichage n'implique aucun calcul ou modification donc c'est juste un affichage simple.

- on va déclarer une variable i à laquelle on affectera une valeur dans la boucle for

- on crée une boucle for pour afficher chaque élements du tableau et pas juste l'indice

- pour l'esthétique d'affiche d'ailleurs on va demander à i de parcourir la taille de tab (peu importe le tableau qu'on passera en argument) et de s'arrêter à sa longueur -2 (-1 pour aller jusqu'au dernier élément du tableau car indice commence à 0) et -2 car on le dernier élément sera affiché sans la virgule après le chiffre car ce sera le dernier chiffre du tableau

- Quand la boucle est arrivée à la longueur de tab -2 alors elle affiche le reste (donc le dernier élément de tab) 



ainsi les deux tableaux seront affichés à chaque fois qu'on leur appliquera la fonction printE
