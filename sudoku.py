'''
    Validacion de un Sudoku
    El usuario introducira las 9 filas del Sudoku, cada una con 9 digitos
    La salida sera Si si el sudoku es valido o No de lo contrario

'''

def noRepetidos(fila):
    lista = list(fila)
    lista.sort()
    for i in range(1,10):
        if (i) != int(lista[i-1]):
            return False
        
    return True
        
    
def validaColumna(entrada):
    
    aux = ''
    for columna in range(9):
        for fila in range(9):
            aux += entrada[fila][columna]
        if not noRepetidos(aux):
            print(f"[!] [ERROR] La columna {fila} no es valida")
            return False
        aux = ''   
    return True
    
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
        elif not noRepetidos(fila):
            print(f"[!] [ERROR] La fila contiene valores REPETIDOS. Vuelve a introducir la fila {i}" )
        else:
            matriz.append(list(fila))
            i += 1
                        
    validaColumna(matriz)

matriz = [['2','9','5','7','4','3','8','6','1'],['4','3','1','8','6','5','9','2','7'],['8','7','6','1','9','2','5','4','3'],['3','8','7','4','5','9','2','1','6'],['6','1','2','3','8','7','4','9','5'],['5','4','9','2','1','6','7','3','8'],['7','6','3','5','2','4','1','8','9'],['9','2','8','6','7','1','3','5','4'],['1','5','4','9','3','8','6','7','2']]    
validaColumna(matriz)    
