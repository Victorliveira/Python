# Programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor ou correto

sexo = 'a'

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
    if sexo not in 'MF':
        print('O sexo foi digitado incorretamente, digite novamente!')
print('O sexo da pessoa foi registrado com sucesso!')
