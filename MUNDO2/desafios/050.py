#Programa que leia 6 num int e mostre a soma apenas daqueles que forem pares. Se o valor digitado for  impar, desconsidere.
soma = 0
for c in range(0,6):
    num = int(input(f'Informe o {c+1}° número: '))
    if num %2 == 0:
        soma = soma + num
print(f'A soma de todos os números pares é igual a {soma}')
