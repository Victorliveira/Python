# Programa que tenha uma tupla única, com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 9.75, 'Caderno', 12.50, 'Borracha', 2.00, 'Mochila', 76.95,'Morango',10.99,'Tinta Guachê', 13.80,'Monitor Dell', 3800.00 )

print('-'*45)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('-'*45)
cont=0
while cont < len(listagem):
    print(f'{listagem[cont]:.<33}', end='')
    print(f'R$ {listagem[cont+1]: >6}')
    cont+=2
print('-'*45)

