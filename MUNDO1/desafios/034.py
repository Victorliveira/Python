#Programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salário superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%

sal = float(input('Informe o salário: '))

if sal <= 1250.00:
    aum = sal +(sal*(15/100))
    print(f'O salário de R${sal:.2f} teve um aumento de 15%, totalizando R${aum:.2f}')
else:
    aum = sal +(sal*(10/100))
    print(f'O salário de R${sal:.2f} teve um aumento de 10%, totalizando R${aum:.2f}')