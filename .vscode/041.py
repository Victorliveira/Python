#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade. até 9 mirim, até 14 infantil, até 19 junio, até 20 sênior, acima master

idade = int(input('Informe sua idade: '))

if idade <= 9:
    print('Categoria Mirim')
elif idade >9 and idade <=14:
    print('Categoria Infantil')
elif idade >14 and idade <=19:
    print('Categoria Junior')
elif idade >19 and idade <=20:
    print('Categoria Sênior')
elif idade >20:
    print('Categoria Master')