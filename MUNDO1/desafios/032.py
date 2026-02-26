# Progrma que leia um ano qlq e mostre se é BISSEXTO
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano%100 == 0:
    bi = ano%400
    if bi == 0:
        print('Ano bissexto')
    else:
        print('Não é bissexto')
else:
    bi = ano%4
    if bi == 0:
        print('Ano bissexto')
    else:
        print('Não é bissexto')


        
