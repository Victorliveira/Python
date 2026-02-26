#Programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "a" ; em que posição ela aparece a primeira vez ; posição que ela aparece a última vez.

frase = input('Digite uma frase: ').strip()

upper = frase.upper()

counta = upper.count('A')
print(f'A letra a aparece {counta} vezes no seu texto.')

ppa = upper.find('A')
print(f'A posição {ppa + 1} é a primeira posição aonde aparece a letra a.')

ppu = upper.rfind('A')
print(f'A posição {ppu + 1} é a última posição aonde aparece a letra a.')