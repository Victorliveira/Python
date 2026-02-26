#Um professor quer sorter a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('Informe o primeiro nome: ')
n2 = input('Informe o segundo nome: ')
n3 = input('Informe o terceiro nome: ')
n4 = input('Informe o quarto nome: ')

nomes = [n1,n2,n3,n4]

ordem = shuffle(nomes)

print(f'A ordem de apresentação será: {nomes}')