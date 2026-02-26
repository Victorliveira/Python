# Programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar no exército, -Se é a hora de se alistar, - Se já passou do tempo de alistamento
# O programa tbm mostra o tempo que falta ou que passou do prazo.
import datetime

ano = int(input('Informe seu ano de nascimento: '))

ano_atual = datetime.date.today().year

tempo = ano_atual - ano

if tempo < 18:
    print(f'Relaxe, você tem {-1*(tempo-18)} anos para se alistar')
elif tempo == 18:
    print('Está na sua hora de se alistar!')
elif tempo > 18:
    print(f'Passou {tempo - 18} anos do seu alistamento!')