# Programa que vai girar 5 números aleatórios e colocar em uma tupla.
# Mostre a listagem de números gerado e também indique o menor e o maior valor que estão na tupla

from random import randint

menornum = maiornum = 0
numal = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os valores sorteados foram: {numal}')
for c in range(0,len(numal)):
    if c == 0:
        menornum = numal[c]
    if menornum > numal[c]:
        menornum = numal[c] 
    if maiornum < numal[c]:
        maiornum = numal[c] 
#print(f'O maior valor sorteado foi {maiornum}')
#print(f'O menor valor sorteado foi {menornum}')
print(f'O maior valor sorteado foi {max(numal)}')
print(f'O menor valor sorteado foi {min(numal)}')