
import numpy as np

matrice_generatrice = [[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
matrice_controle = [[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]]
mots = [[1],[0],[1],[1]]

A = np.array(matrice_generatrice)
print(A.shape)

B = np.array(mots)
print(B.shape)

C = A.dot(B)%2
print(C)

D = np.array(matrice_controle)

E = D.dot(C)%2
print(E)


#lecture du fichier source.txt
##f_source = open("source.txt", "r")
##contenu_source = f_source.read()

#Lecture d'une matrice de codage
##f_matrice_codage = open("matrice_codage.txt", "r")
##contenu_matrice_codage = f_matrice_codage.read()

##tab_matrice_codage = contenu_matrice_codage.split("\n")
##tab_matrice_codage = map(int, tab_matrice_codage)

#Creation de mots de taille 3
##mots = re.findall('....', contenu_source)

#for element_matrice in tab_matrice_codage:
#    print(element_matrice)


#Fermeture des fichiers ouverts
##f_matrice_codage.close()
##f_source.close()