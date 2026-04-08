# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

jogadores = list()
campeonato = dict()
partidajog = list()
partida = dict()
gols = list()
total = 0
while True:
    campeonato['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {campeonato['nome']} jogou? '))

    for c in range(partidas):
        partida[f'partida {c+1}'] = int(input(f'Quantos gols na partida {c+1}? '))
        total += partida[f'partida {c+1}']
        gols.append(partida.copy()[f'partida {c+1}'])

    campeonato['gols'] = gols[:]
    campeonato['total'] = total
    partidajog.append(partida.copy())
    jogadores.append(campeonato.copy())
    partida.clear()
    gols.clear()
    parar = str(input('Deseja Continuar? [S/N] '))[0].upper()
    while parar not in ('SN'):
        print('Operação Inválida. Digite novamente!')
        parar = str(input('Deseja Continuar? [S/N] '))[0].upper()
    if parar == 'N':
        break
    total = 0


print('-='*30)

print(f"{'cod':<3}{'nome':^10}{'gols':<20}{'total':>5}")
for pos, v in enumerate(jogadores):
    print(f"{pos:<3}", end='')
    print(f"{jogadores[pos]['nome']:^10}", end='')
    print(f"{str(jogadores[pos]['gols']):<20}", end='')
    print(f"{jogadores[pos]['total']:^5}", end='')
    print()

while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    while dados > len(jogadores)-1:
        print('Operação Inválida. Digite novamente!')
        dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    
    cont = 0
    for c in partidajog[dados]:
        print(f'    => Na partida {c}, fez {partidajog[dados][f'partida {cont+1}']} gols.')
        cont+=1
            
    
print('<<ENCERRADO>>')