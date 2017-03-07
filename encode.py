
import numpy as np
import re


def encode(a, b):
    a = np.array(matrice_generatrice)
    b = np.array(mots)
    c = a.dot(b) % 2

    f_mot_de_code = open("mot_de_code.txt", "w")
    f_mot_de_code.write(c.__str__())
    f_mot_de_code.close()

    return c

def decode(a, b, c, d):
    c = np.array(matrice_controle)
    d = encode(a,b)
    e = c.dot(d) % 2
    return e


#D = np.array(matrice_controle)

#E = D.dot(C)%2
#print(E)


#lecture du fichier source.txt
f_source = open("source.txt", "r")
contenu_source = f_source.read()


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

if __name__ == "__main__":
    matrice_generatrice = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]]
    matrice_controle = [[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]]
    mots = [[1], [0], [1], [1]]

    print("Mot de code :")
    mot_code = encode(matrice_generatrice, mots)
    print(mot_code)
    #print('{}{}{}{}{}{}{}'.format(*mot_code))

    print("Y a t-il des erreurs ? :")
    mot_avec_erreur = decode(matrice_generatrice, mots, matrice_controle, mot_code)
    print(mot_avec_erreur)

