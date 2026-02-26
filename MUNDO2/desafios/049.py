#Refaça desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agr utilizando for.

tab = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print(tab, '*',c,'=',c*tab)