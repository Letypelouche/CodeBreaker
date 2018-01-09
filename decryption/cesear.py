# coding: utf-8

def decaltxt(txt,decal):
    # fonction pour retrouver un texte avec dealage de x
    ret = ""
    for i in txt:
        val = ord(i)
        print val
        if (val in range(65, 90)) | (val in range(97, 122)):
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

