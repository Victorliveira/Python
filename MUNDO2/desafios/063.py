# Programa que leia um num n inteiro qlq e mostre na tela os n primeiros elementos de uma sequência de fibonacci. 

print('='*40)
print('SEQUÊNCIA DE FIBONACCI')
print('='*40)

ele = int(input('Quantos elementos deseja ver? '))

num = 0
numan = 1
n = 0

while n != ele:
    if n < 1:
        print(num, end=' -> ')
        n+=1
    elif n >= 1:
        print(num + numan, end=' -> ')
        num += numan
        numan = num - numan
        n+=1
print('ACABOU')