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


for c in matriz:
    for num in c:
        if num %2 == 0:
            somap += num

#printa a matriz        
for c in matriz:
    print(c)

print(f'A soma de todos os números pares é igual a {somap}')
print(f'O maior valor da linha 2 é {max(matriz[1])}')
print(f'A soma da terceira coluna é igual a  ')