# Programa que le 2 num int e compare-os, mostrando na tela uma mensagem. -O primeiro valor é maior, -O segundo valor é maior - Não existe valor maior, os dois são iguais

num = int(input('Informe um número inteiro: '))
num_com = int(input('Informe outro número inteiro '))

if num > num_com:
    print('O primeiro valor é maior!')
elif num < num_com:
    print('O segundo valor é maior!')
elif num == num_com:
    print('Não existe valor maior, os dois são iguais')
