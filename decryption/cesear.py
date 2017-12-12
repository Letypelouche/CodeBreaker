def change(cara,dec) :
    # cara = caractere a changer, dec le decalage a faire
    cara = cara+dec
    if ((cara >90 & cara <141) | cara > 172) :
        cara = cara - 26
    return cara