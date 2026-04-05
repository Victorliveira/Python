# Aprimore o desafio 86, mostrando no final: a- soma de todos os valores pares digitados. b- soma dos valores da terceira coluna. c- O maior valor da segunda linha

matriz = []
#tamanho da matriz
tmatriz = 3
somap = somac = 0

for l in range(tmatriz):
    linha = []
    for v in range(1,4):
        linha.append(int(input(f'Digite um número para a linha {l+1} da coluna {v}: ')))
    matriz.append(linha)

#soma todos os números pares
for c in matriz:
    for num in c:
        if num %2 == 0:
            somap += num

#soma todos os números da coluna 3
for pos,v in enumerate(matriz):
    somac+= matriz[pos][2]

print('-='*30)
#printa a matriz        
for linha in matriz:
    for pos,v in enumerate(linha):
        print(f'[{v:^5}]', end=' ')
        if pos ==2:
            print()
print('-='*30)

print(f'\nA soma dos valores pares é igual a {somap}')
print(f'A soma da terceira coluna é igual a {somac}')
print(f'O maior valor da segunda linha 2 é {max(matriz[1])}')
