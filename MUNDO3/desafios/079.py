# Programa onde o usuário leia vários num e cadastre-os numa lista. Caso o número já exista lá dentro, ele n será adicionado. No final, serâo exibidos todos os valores únicos digitado em ordem crescente.

num =list()

while True:
    numad = int(input('Digite um valor: '))
    if numad not in num:
        num.append(numad)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não foi adicionado!')
    parar = input('Deseja parar? S/N ').upper()
    while parar not in 'SN':
        print('Operação incorreta, digite novamente')
        parar = input('Deseja parar? S/N ').upper()
    if parar in 'S':
        break
num.sort()
print(f'Essa é a lista em ordem crescente: {num}')
num.sort(reverse=True)
print(f'Essa é a lista em ordem descrescente: {num}')

