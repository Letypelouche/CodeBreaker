from math import *

# donne un pourcentage de mot concordant avec le texte témoins
def compare(txt):
    cpt_mot = 0.0
    cpt_percent = 0.0
    with open("../ressources/texte_temoin.txt", "r") as f:
        fichier = f.read()
        for i in txt.split():
            cpt_mot += 1.0
            for j in fichier.split():
                if j == i:
                    cpt_percent += 1.0
                    break
    return trunc((cpt_percent/cpt_mot)*100)

# retourne si le pourcentage de vraisemblabilité est au dessus de 5
def fra(txt):
    return 5 < compare(txt)