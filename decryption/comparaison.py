import os.path

def compare(txt):
    cpt_mot = 0
    cpt_percent = 0
    with open("../ressources/texte_temoin.txt", "r") as f:
        fichier_entier = f.read()
        return fichier_entier.split()
    for i in txt.split():
        cpt_mot += 1
    return i
