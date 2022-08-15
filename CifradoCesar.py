# Cifrado César

def cifradoCesar(text):
    
    cifrado = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cifrado += chr(code)
    return cifrado

cifrar = input("Ingresa tu mensaje a cifrar: ")
print(cifradoCesar(cifrar))

def descrifradoCesar(cifrado):
    text = ''
    for char in cifrado:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    return text

descifrar = input("Ingresa tu mensaje a descrifrar:")
print(descrifradoCesar(descifrar))
