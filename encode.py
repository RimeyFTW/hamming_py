import os

#lecture du fichier source.txt
fichier_source = open("source.txt", "r")
contenu_source = fichier_source.read()

#TEST
print(contenu_source)



fichier_source.close()