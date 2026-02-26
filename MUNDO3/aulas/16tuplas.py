# TUPLAS

# As Tuplas são IMUTÁVEIS
# Tuplas recebem vários valores e são criadas usando parênteses
lanche = ('Hambúrguer','Suco','Pizza','Pudim')
print(len(lanche))
print(lanche[1:])

for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}') 

print(sorted(lanche)) # print em ordem alfabética

a = (2,5,4)
b = (5,8,1,2)
c = a+b

print(c.count(5)) # Mostra quantidade de vezes que o num 5 aparece na tupla

print(c.index(8)) # Mostra a posição do num 8 dentro da tupla

pessoa = ('victor', 39, 'M', 85.5) # Tuplas podem ter vários tipos de dados dentro

del(pessoa) #del serve para apagar uma variável
print(pessoa)