from decryption.utilita import *
from decryption.cesear import *
from decryption.filtres import *


def decry_jojo(txt):
    tmp_char = recurente(txt)
    return decaltxt(txt,101-ord(tmp_char))


def decry_hexa(txt):
    return exa_txt(txt)

print decry_hexa("4242424200000042")
print decry_jojo("MéSdlph oh ehxuuh")
print (ord("'"))