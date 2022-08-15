# Procesador de numeros
# Acepta una secuencia de numeros float separados por espacios y devuelve la suma

linea = input("Ingresa una línea de números, sepáralos con espacios: ")
if linea:
    strings = linea.split()
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        print("El total es:", total)
    except:
        print(substr, "no es un numero.")
else:
    print("No ha introducido ninguna secuencia de numeros")