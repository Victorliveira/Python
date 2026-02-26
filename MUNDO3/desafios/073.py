# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a- Apenas os 5 primeiros colocados. b-Os últimos 4 colocados da tabela. c- Uma lista com os times em ordem alfabética. d-Posição na tabela que está o time da Chapecoense

br = ('Palmeiras','São Paulo','Fluminense','Bahia','Corinthians','Athletico-PR','Bragantino','Chapecoense','Mirassol','Coritiba','Flamengo','Botafogo','Grêmio','EC Vitória','Atlético-MG','Remo','Vasco da Gama','Santos','Internacional','Cruzeiro')
print('-='*25)
print(f'Lista de times do Brasileirão: {br}')
print('-='*25)
print(f'Os 5 primeiros são {br[0:5]}')
print('-='*25)
print(f'Os 4 últimos são {br[-4:]}')
print('-='*25)
print(f'Times em ordem alfabética {sorted(br)}')
print('-='*25)
print(f'O Chapecoense está na {br.index("Chapecoense")+1}° posição')

