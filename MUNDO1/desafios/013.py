#Algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

sal = float(input('Informe o salário do funcionário: '))

aumento = (sal + (sal * ( 15/ 100)))

print(f'O salário de {sal}R$, com um aumento de 15%, fica por {aumento:.2f}R$!')