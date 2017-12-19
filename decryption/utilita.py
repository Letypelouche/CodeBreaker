from filtres import *

def recurente(txt):
    txt = txt.toLowerCase()
    tmp_nb = 0
    for i in range(0,25):
        if tmp_nb < txt.count(exa_txt(i+97)):
            rtn = exa_txt(i+97)
            tmp_nb = txt.count(exa_txt(i+97))
    return rtn