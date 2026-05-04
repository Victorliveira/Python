# modularização surgiu nos anos 60 quando os sistemas estavam ficando maiores
# foco: dividir um programa grande/ aumentar legibilidade

#Criado um modulo próprio para as funções chamado uteis.py

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')



# Quando se tem muitas funções dentro de um módulo, é possível divido-lo por assuntos. isso é chamado de pacote

# é possível importar dentro de um pacote um assunto especifico