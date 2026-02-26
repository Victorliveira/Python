#Operadores Aritméticos

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
mult = n1 * n2
divi = n1 / n2
divin = n1 // n2
pote = n1 ** n2

print(f'A soma é {soma}, \n a multiplicação é {mult}, a divisão é {divi:.3f}', end=' ') # \n quebra a linha end=, define oq vai aparecer no final do texto sem quebrar linha    
print(f'A divisão inteira é {divin}, a potência é {pote}')