#!/usr/bin/env python3

"""Exercicio de Tabuda"""
__author__:"Lucas"
__version__:"1.0.0"


numeros = range(1,11)

for numero in numeros:
    print("Tabuada do: ", numero)
    for outro_num in numeros:
        print(outro_num, " * ", numero, " = ", outro_num * numero)
    print("----------------")