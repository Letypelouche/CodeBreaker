# coding: utf-8
from decryption.utilita import *
from decryption.cesear import *
from decryption.filtres import *

# decrypte avec la methode cesear
def decry_jojo(txt):
    tmp_char = recurente(txt)
    return decaltxt(txt,101-ord(tmp_char))

# decrypte avec la methode hexa
def decry_hexa(txt):
    return exa_txt(txt)