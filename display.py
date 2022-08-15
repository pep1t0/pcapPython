'''
SUBJECT:
Seguramente has visto un display de siete segmentos.

Es un dispositivo (a veces electrónico, a veces mecánico) diseñado para presentar un dígito decimal utilizando un subconjunto de siete segmentos.
Si aún no sabes lo qué es, consulta la siguiente liga en Wikipedia artículo.

Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.
'''

def display(numero):
    
    patrones = [['  #', '###', '###', '# #', '###', '###', '###', '###', '###', '###'],
                ['  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #', '# #'], 
                ['  #', '###', '###', '###', '###', '###', '  #', '###', '###', '# #'],
                ['  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #', '# #'], 
                ['  #', '###', '###', '  #', '###', '###', '  #', '###', '###', '###']]
    
    for j in range(5):            
        for i in str(numero):
            print(patrones[j][int(i)-1],end='   ')
        print(f"")

display(123)
display(9081726354)