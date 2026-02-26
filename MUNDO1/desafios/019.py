#Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

n1 = input('Informe o primeiro nome: ')
n2 = input('Informe o segundo nome: ')
n3 = input('Informe o terceiro nome: ')
n4 = input('Informe o quarto nome: ')

nomes = [n1,n2,n3,n4]

escolhido = choice(nomes)

print(f'O escolhido foi {escolhido}')