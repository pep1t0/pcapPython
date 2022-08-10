# main.py
from sys import path

print('Esta es la variable path',path)
path.append('/usr/local/lib/modules')
print('Nueva variable path',path)

from module import suml, prodl, __counter

print('Contador antes de invocarse',__counter)
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

print('Valor del contador:',__counter)