#Programa que le quanto dinheiro uma pessoa tem e mostre quantos dólares pode comprar

din = float(input('Quantos reais deseja converter? '))

conversao = din / 5.42

print(f'Com {din}R$ você consegue comprar {conversao:.2f} dólares')