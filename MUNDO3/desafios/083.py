#Programa onde o usuário digite uma expressão qlq que use parênteses.Seu app deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


exp = input("Digite uma expressão algoritimíca: ")

expv = []

for c in exp:
    if c == '(':
        expv.append(c)
    if c == ')':
        if expv:
            expv.pop()    
        else:
            expv.append(c)
            break


if not expv:
    print('Expressão correta')
else:
    print('Expressão incorreta')

    