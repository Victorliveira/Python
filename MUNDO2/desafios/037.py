#Programa que le um número inteiro qlq e peça para o usuário escolher qual será a base de conversão: 1-binário 2-octal 3-hexadecimal
import math

num = int(input('Informe um número: '))
print('-1 binário\n-2 octal\n-3 hexadecimal')
esc = input('Escolha sua base de conversão:')

bin = bin(num)
octal = oct(num)
hexa = hex(num)

if esc == '1':
    print(f'O número {num}, convertido para binário é {bin[2:]}')
elif esc == '2':
    print(f'O número {num}, convertido para octal é {octal[2:]}')
elif esc == '3':
    print(f'O número {num}, convertido para hexadecimal é {hexa[2:]}')
else:
    print('OPÇÃO INVÁLIDA')

