# Programa que leia 5 valores num e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num =[]
for v in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {v}: ')))

print('-='*30)
print(f'Você digitou os valores {num}')

print(f'O valor {max(num)} foi o maior digitado e está nas posições ', end='')
for pos,v in enumerate(num):
    if v== max(num):
        print(f' {pos}...', end='')


print(f'\nO valor {min(num)} foi o menor digitado e está nas posições', end='')
for pos,v in enumerate(num):
    if v == min(num):
        print(f' {pos}...', end='')

