#Progrma que le um número inteiro e mostre na tela se é PAR ou IMPAR

num = int(input('Escolha um número: '))

if num%2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')