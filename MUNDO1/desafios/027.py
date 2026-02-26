#Programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip()

split = nome.split()

print(f'Primeiro nome: {split[0]}')

unome = nome.rfind(' ')
sobrenome = nome[(unome + 1):]

print(f'Último nome: {sobrenome}')

#print(f'Último nome: {split[len(split)-1]}')