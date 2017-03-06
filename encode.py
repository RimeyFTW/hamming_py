import string
import re

#lecture du fichier source.txt
f_source = open("source.txt", "r")
contenu_source = f_source.read()

#Creation de mots de taille 3
mots = re.findall('...', contenu_source)

#Creation d'une matrice de codage
f_matrice_codage = open("matrice_codage.txt", "r")
contenu_matrice_codage = f_matrice_codage.read()


#TEST
print(contenu_source)
print(mots)
print(contenu_matrice_codage)

#Fermeture des fichiers ouverts
f_matrice_codage.close()
f_source.close()