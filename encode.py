
import numpy as np
import re

def encode():
    a = np.array(matrice_generatrice)
    b = np.array(mot)
    c = a.dot(b) % 2

    f_mot_de_code = open("mot_de_code.txt", "w")
    f_mot_de_code.write(''.join(str(word) for word in c))
    f_mot_de_code.close()
    return c

def decode():
    c = np.array(matrice_controle)
    d = encode()
    e = c.dot(d) % 2
    return e


if __name__ == "__main__":
    #Attribut
    matrice_generatrice = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]]
    matrice_controle = [[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]]
    mot = [1,1,1,1]

    f_source = open("source.txt", "r")
    contenu_tab_source = f_source.read()
    #Supprime les \n du fichier source
    contenu_tab_source_sans_retour = contenu_tab_source.replace("\n", "")

    f_msg = open("message.txt", "w")
    #Separe le mot de "source.txt" en plusieurs mots de longueurs 4
    mot_source = re.findall('....', contenu_tab_source_sans_retour)

    for mot in mot_source:
        #Permet de stocker le mot dans un tab --> AVANT: 1111, APRES : [1,1,1,1]
        mot = [int(e) for e in mot]

        #Mot de code
        mot_code = encode()

        mot_avec_sans_erreur = decode()

        #Permet de verifier si mot_avec_sans_erreur contient une erreur ou non -> Si = [0,0,0] il n'y a pas d'erreur, sinon il y en a une
        if (mot_avec_sans_erreur == np.array([0, 0, 0])).all():
            #On ne garde que les 4 premiers bits du mot de code
            mot_correct = mot_code[0:4]
            #On stock chaque message dans "message.txt"
            f_msg.write(''.join(str(w) for w in mot_correct))

    f_msg.close()
    f_source.close()

    f_message_entier = open("message.txt", "r")
    message = f_message_entier.read()
    f_message_entier.close()

    f_message = open("message.txt", "w")
    compteur = 0

    #Permet d'ajouter un \n tout les 90 caracteres (afin de retrouver un space invader)
    for elt in message:
        compteur += 1
        if compteur % 90 == 0:
            f_message.write(elt)
            f_message.write('\n')

        else:
            f_message.write(elt)

    f_message.close()

