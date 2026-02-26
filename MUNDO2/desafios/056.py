#Programa que leia o nome, idade, sexo de 4 pessoas, no final do programa, mostre:
# A média de idade do grupo , qual o nome do homem mais velho. Quantas mulhers têm menos de 20 anos
idade_c = 0 #contador das idades
idade_h = 0 # variável para salvar a idade do homem mais velho
nome_h = 'a'# variável para salvar o nome do homem mais velho
cont_m = 0 # contador de mulheres com menos de 20 anos

for c in range(0,4):
    print(f'---- {c+1}° PESSOA ----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    print('[ 1 ] - Mulher\n[ 2 ] - Homem')
    sexo = int(input('Sexo: '))
    idade_c += idade
    if sexo == 2 and idade > idade_h:
        idade_h = idade
        nome_h = nome
    elif sexo == 1 and idade < 20:
        cont_m += 1


print(f'\nA média de idade do grupo é de {idade_c/4:.1f} anos')
print(f'O {nome_h} é o homem mais velho e tem {idade_h} anos')
print(f'Existe {cont_m} mulheres dentro do grupo com menos de 20 anos.')

