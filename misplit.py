def misplit(strng):
    
    salida = []
    tmp = ''
    
    if strng:
        for i in strng:
            if i != ' ':
                tmp += i
            else:
                if tmp:
                    salida.append(tmp)
                    tmp = ''
        if tmp: salida.append(tmp)
    return salida

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))