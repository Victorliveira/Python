# Programa que leia o comprimento de 3 retas e dia ao usuário se elas podem ou não formar um triângulo.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

n1n2 = num1 + num2
n1n3 = num1 + num3
n2n3 = num2 + num3

if n1n2 > num3 and n1n3 > num2 and n2n3 > num1:
    print('É possível criar um triangulo usando esses valores!')
else:
    print('Não é possível criar um triangulo usando esses valores!')
    