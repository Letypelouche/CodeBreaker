

def decaltxt(txt,decal):
    # fonction pour retrouver un texte avec dealage de x
    ret = ""
    for i in txt:
        if (ord(i) < 91 & ord(i) > 64) | (ord(i) > 96 & ord(i) < 123):
            print(i)
            print(ord(i))
            ret = ret + change(i, decal)
        else:
            ret = ret + i
    return ret


def change(cara, dec):
    # fonction de decalage de caratere
    # cara = caractere a changer, dec le decalage a faire
    ret = ord(cara)+dec
    if (ret > 90 & ret < 97) | ret > 122:
        ret = ret - 26
    return chr(ret)

