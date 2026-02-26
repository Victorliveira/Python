# Programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Digite seu nome: ').strip()

upper = nome.upper()

print('Seu nome tem Silva?', 'SILVA' in upper)