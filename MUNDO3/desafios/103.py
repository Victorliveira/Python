# Programa que tenha uma função chamado ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou
# Programa deverá ser capaz de mostrar a ficha do jogador, mesmo que alfum dado não tenha sido informado corretamente.

def ficha(nome,gol):
    if not nome:
        nome = '<desconhecido>'
    if not gol:
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

print('-'*20)
n = str(input('Nome do Jogador: ')).capitalize()
g = input('Número de Gols: ')

ficha(n,g)