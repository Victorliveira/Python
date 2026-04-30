# Programa que tenha uma função chamado ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou
# Programa deverá ser capaz de mostrar a ficha do jogador, mesmo que alfum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>',gol=0):
    """
    -> Apresenta uma ficha técnica com o nome do Jogador e quantidade de gols
    :param nome: Nome do Jogador
    :param gol: Quantidade de gols
    """



    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

print('-'*20)
n = str(input('Nome do Jogador: ')).capitalize()
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g=0
if n.strip()== '':
    ficha(gol=g)
else:
    ficha(n,g)
