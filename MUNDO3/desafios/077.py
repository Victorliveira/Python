# # Programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, deve mostrar para cada palavra quais são suas voguais.

palavras = ('agua', 'curso', 'matematica','festa','passear','estranho','fera','psicologia','dicotomia')

vogais = 'VALIDADOR DE VOGAIS'
print('='*50)
print(f'{vogais:^50}')
print('='*50)


for num, index in enumerate(palavras):
    print(f'Na palavra {palavras[num].upper()} temos as vogais:', end=' ')
    for c in range(0,len(index)):
        if index[c] in ('aeiou'):
            print(index[c], end=' ')
    print('')