#Programa que mostre na tela todos os números pares que estão entre 1 e 50

for c in range(2,51,2):
    print(c, end=' ')
print('\nAcabou')


for c in range(1,51): # Dessa forma o sistema usa mais do processador do q o método de cima
    print('.', end=' ')
    if c % 2 == 0:
        print(c, end=' ')