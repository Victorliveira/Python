# Programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta

linha1 = list()
linha2 = list()
linha3 = list()
matriz = list()

matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
cont= 0

# cadastra o número em todos os parâmetros
while True:
    for v in range(1,4):
        matriz[cont].append(int(input(f'Digite um número para a linha {cont+1} coluna {v}: ')))    
    cont+=1
    if cont ==3:
        break

#printa em forma de matriz
for linha in matriz:
    print(linha)
    