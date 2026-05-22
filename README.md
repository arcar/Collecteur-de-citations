# Collecteur-de-citations
Collecteur de citations - Automatisation de contenu web



1ère étape : Création d'un script python 
2ème étape : On crée en amont un variable contenant une liste nommée citation
3ème étape : On initialise une boucle se limitant à 5 itérations
4ème étape : Dans cette boucle, une variable message va réaliser une requète à chaque itération à http://api.quotable.io/random, 
            dans le même temps la variable message va se stocker elle même dans la variable data qui prend le .json et dans le même temps à chaque itération, nous ajoutons à notre liste les combinaisons clés, valeurs ayant pour valeur les balises 'author' et 'content' de l'API en question
5ème étape : On crée une variable slide_html, à la suite de cela, nous créons une boucle qui fait parcourir la variable quote   sur la liste citations. Pour chaque itération, 'content' et 'author' à l'intérieur de notre liste se mettront à jour en prenant la valuer de 'quote'. Enfin, nous stockons à chaque tour, ces valeurs dans des balises <div> de notre code html pour les faire afficher dans leur bloc respectif et unique.
6ème étape : Nous écrivons notre code html hors de toutes boucles 
7ème étape : Pour finir, nous définissons le nom du fichier html lors de sa génération et nous demandons au script de l'écrire
