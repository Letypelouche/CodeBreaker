# coding: utf-8
from filtres import *
from string import *

# detruit tout caractère non ascii dans le texte
def kill_non_uni(txt):
    txt2 = ""
    for i in txt:
        if ord(i) < 128:
            txt2 += i
    return txt2

# regarde la lettre la plus recurente dans le texte
def recurente(txt):
    txt = kill_non_uni(lower(txt))
    tmp_nb = 0
    rtn = ""
    for i in range(0,25):
        if tmp_nb < txt.count(unichr(i+97)):
            rtn = unichr(i+97)
            tmp_nb = txt.count(unichr(i+97))
        replace(txt,unichr(i+97), "")
        if tmp_nb > len(txt):
            break
    return rtn