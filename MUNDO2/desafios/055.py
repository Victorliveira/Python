#Programa que leia o peso de 5 pessoas e mostre qual foi o maior e menor peso informado.
max_peso = 0
min_peso = 0


for c in range(1,6):
    peso = float(input(f'Informe o {c}° peso: '))
    if c == 1:
        max_peso = peso
        min_peso = peso
    else :
        if peso > max_peso:
            max_peso = peso
        elif min_peso > peso:
            min_peso = peso

print(f'\n{max_peso}KG foi o maior peso lido')
print(f'{min_peso}KG foi o menor peso lido')