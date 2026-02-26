#Programa que le a velocidade de um carro. Se passar de 80km, mostre uma mensagem informando que foi multado. A multa vai custa R$7,00 por cada KM acima do limite

km = float(input('Informe a velocidade do carro: '))

if km > 80:
    multa = 7*(km - 80)
    print('A velocidade limite é de 80km')
    print(f'Você foi multado, a sua multa é de R${multa:.2f}')
else:
    print('Tenha um Bom dia, continue dirigindo com cuidado!')