#!/usr/bin/env python3

""" module.py - an example of Python module """

__counter = 0

def suml(list):
    global __counter
    __counter += 1
    print(__counter)
    sum = 0
    for el in list:
        sum += el
        
    return sum

def prodl(list):
    global __counter	
    __counter += 1
    print(__counter)
    prod = 1
    for el in list:
        prod *= el
    
    return prod

if __name__ == "__main__":
	print("Ejecucion directamente como modulo")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)