#Programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas

km = int(input('Informe o KM da viagem: '))

if km <=200:
    cal = km * 0.50
    print(f'O preço da passagem é de R${cal}')
else:
    cal = km * 0.45
    print(f'O preço da passagem é de R${cal}')