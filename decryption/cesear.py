

def decaltxt(txt):
    # fonction pour retrouver un texte avec dealage de x
    ret = ""
    for i in txt:
        ret = ret + change(i, 1)
    return ret


def change(cara, dec):
    # fonction de decalage de caratere
    # cara = caractere a changer, dec le decalage a faire
    ret = ord(cara)+dec
    if (ret > 90 & ret < 97) | ret > 122:
        ret = ret - 26
    return chr(ret)

