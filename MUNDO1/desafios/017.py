#Faça um programe que leia o compimento do cateto oposto e do cateto adkacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa 
from math import hypot

co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))

print(f'A hipotenusa é igual: {hypot(co,ca):.2f}')
