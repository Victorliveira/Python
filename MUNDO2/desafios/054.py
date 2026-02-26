#Programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

import datetime

maior = 0
menor = 0
ano_atual = datetime.date.today().year

for c in range(0,7):
    ano = int(input(f'Em que ano a {c+1}° pessoa nasceu? '))
    if ano_atual - ano >=21:
        maior += 1
    elif ano - ano_atual <21:
        menor +=1
print(f'\n{maior} pessoas atingiram a maioridade')
print(f'{menor} pessoas não atingiram a maioridade ')
