'''
Ejemplo de control de excepciones
'''
def readint(prompt, min, max):
    
    while True: 
        try:
            print(prompt)
            x = int(input())
            assert x >= -10 and x <=10
            return x
        except ValueError:
            print("Debes ingresar un valor entero")
        except AssertionError:
            print("Valores fuera de rango")
    

v = readint("Ingresa un numero de -10 a 10: ", -10,10)
print('El numero es', v)