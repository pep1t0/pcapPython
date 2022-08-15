'''
    Validacion de un Sudoku
    El usuario introducira las 9 filas del Sudoku, cada una con 9 digitos
    La salida sera Si si el sudoku es valido o No de lo contrario

'''

def validaFila(fila):
    lista = list(fila)
    lista.sort()
    for i in range(1,10):
        if (i) != int(lista[i-1]):
            return False
        
    return True
        
    
# def validaColumna(entrada):
    
# def valida3x3(entrada):
    
def entradaValores():
    
    matriz = []
    i = 1
    while i < 10:
        fila = input(f"[?] Introduce la fila {i} : ")
        if not fila.isdigit():
            print(f"[!] [ERROR] La fila solo puede contener NUMEROS. Vuelve a introducir la fila {i}")
        elif len(fila) >9:
            print(f"[!] [ERROR] La fila tiene mas de 9 digitos. Vuelve a introducir la fila {i} ")
        elif not validaFila(fila):
            print(f"[!] [ERROR] La fila contiene valores REPETIDOS. Vuelve a introducir la fila {i}" )
        else:
            matriz.append(list(fila))
            i += 1
                        
    return matriz
    
salida = entradaValores()    
print(salida)