#Programa  que leia dos valores e mostre um menu na tela: 
#1 somar 2 multiplicar 3 maior valor 4 novos números 5 sair do programa. Programa deverá realizar a operação solicitada em cada caso.

num1 = 0
num2 = 0
esc = 0
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

while esc != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Novos números
[5] Sair''')
    esc = int(input('Informe a operação desejada: '))
    if esc == 1:
        print(f'A soma de {num1} e {num2} é igual a {num1+num2}')
    if esc == 2:
        print(f'A multiplicação dos números é igual a {num1*num2}')
    if esc == 3:
        if num1 > num2:
            print(f'O maior valor é {num1}')
        if num2 > num1:
            print(f'O maior valor é {num2}')
    if esc == 4:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
    if esc not in (1,2,3,4,5):
        print('Operação inexistente, digite novamente!')
print('Programa Finalizado')


