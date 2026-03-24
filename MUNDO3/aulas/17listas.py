# listas são feitas com []

lanche = ['burguer','suco','pizza','pudim']
print(lanche)
lanche[3] = 'picole' # listas são MUTÁVEIS
print(lanche)

lanche.append('cookie') # append adiciona um elemento no final da lista
print(lanche)
lanche.insert(2,'sushi')# insert adiciona um elemento na chave desejada
print(lanche)

del lanche[3] # del serve para eliminar um elemento indicando sua chave
print(lanche)
lanche.pop(3)# por padrão elimina o último elemento, mas pode ser parametrizado para eliminar a chave desejada
print(lanche)
lanche.remove('sushi') # o método remove usa o VALOR invés da chave
print(lanche)

valores = list(range(4,11)) # criando uma lista usando range
print(valores)

num =[8,2,5,3,9,3,0]
num.sort()# deixa os elementos da lista em ordem
num.sort(reverse=True)# deixa a lista em ordem ao contrário

lista = [2,4,3,7]
lisb = lista[:] # copia os valores
lisb[2] = 8
print(lista)
print(lisb)

