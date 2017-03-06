import string
import re

#Methode addition binaire
def add(a, b):
    if a == b:
        return 0
    else :
        return a+b

#lecture du fichier source.txt
f_source = open("source.txt", "r")
contenu_source = f_source.read()

#Lecture d'une matrice de codage
f_matrice_codage = open("matrice_codage.txt", "r")
contenu_matrice_codage = f_matrice_codage.read()

#Creation de mots de taille 3
mots = re.findall('...', contenu_source)

for element_matrice in contenu_matrice_codage:
    print (element_matrice)

#TEST
print(contenu_source)
print(mots)
print(contenu_matrice_codage)


#Fermeture des fichiers ouverts
f_matrice_codage.close()
f_source.close()