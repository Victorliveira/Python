# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira

from math import trunc

num = float(input("Digite um número: "))
print(f' O número {num} tem a parte inteira {trunc(num)}')
