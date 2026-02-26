# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar o tipo de triângulo que será formado. Equilátero: todos lados iguais, isósceles: dois lados iguais. Escaleno: todos os lados diferentes.

# Programa que leia o comprimento de 3 retas e dia ao usuário se elas podem ou não formar um triângulo.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

n1n2 = num1 + num2
n1n3 = num1 + num3
n2n3 = num2 + num3

if n1n2 > num3 and n1n3 > num2 and n2n3 > num1:
    print('É possível criar um triangulo usando esses valores!')
    if num1 == num2 == num3:
        print('Com esses valores é possível criar um triângulo Equilátero')
    elif num1 == num2 and num1 != num3 or num2 == num3 and num2 != num1 or num3 == num1 and num1 != num2:
        print('Com esses valores é possível criar um triângulo Isósceles')
    elif num1 != num2 != num3 != num1:
        print('Com esses valores é possível criar um triângulo Escaleno')
else:
    print('Não é possível criar um triangulo usando esses valores!')
    