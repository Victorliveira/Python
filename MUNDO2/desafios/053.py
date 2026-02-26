# Programa que leia uma frase qlq e diga se ela é um palíndromo, desconsiderando espaços.

frase = input('Escreva uma frase: ').replace(',','').strip().upper().split()
tot = 0
frase_junta = ''.join(frase)
print(f'O inverso de {frase_junta} é {frase_junta[::-1]}')
for c in range(0,len(frase_junta)):
    i = frase_junta[0:] # valida do começo para o final
    j = frase_junta[::-1] # valida do final para o começo
    if i == j:
        tot += 1
if tot == len(frase_junta):
    print('Temos um palíndromo!')
elif tot != len(frase_junta):
    print('A frase digitada não é um palíndromo')
        