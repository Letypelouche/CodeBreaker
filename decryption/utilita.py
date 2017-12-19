from filtres import *
from string import *
def recurente(txt):
    txt = lower(txt)
    tmp_nb = 0
    for i in range(0,25):
        if tmp_nb < txt.count(unichr(i+97)):
            rtn = unichr(i+97)
            tmp_nb = txt.count(unichr(i+97))
        replace(txt,unichr(i+97),"")
        if tmp_nb > count(txt):
            break
    return rtn