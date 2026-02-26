# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar oo valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

casa = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe seu salário: R$'))
ano = int(input('Em quantos anos pretende pagar a casa? '))

prestacao = casa/(ano * 12)
print(f'Para pegar uma casa de R${casa:.2f} em {ano} anos, a prestação será de R${prestacao:.2f}')
if prestacao > sal * 0.30:
    print('Seu empréstimo foi negado!')
else:
    print('Parabéns, seu empréstimo foi aprovado!')