#Algoritmo que le um preço de um produto e informa o novo preço com 5% de desconto
import math


preco = float(input('Informe o preço do produto: '))
desconto = float(input('Informe a porcentagem de desconto: '))

novo = preco * ( desconto / 100 )

print(f'O produto de {preco}R$, com {desconto}% de desconto fica R${preco - novo:.2f}')