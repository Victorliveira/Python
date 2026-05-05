# Crie um pacote chamado utilidadesCeV que tenha dois módulos inteiros chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107 até o 109 para o primeiro pacote e mantenha tudo funcionando

from ex111.utilidadesCeV import moeda

n = float(input('Digite o preço: R$'))
moeda.resumo(n,80,35)