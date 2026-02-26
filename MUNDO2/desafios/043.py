# Programa que le o peso e altura de uma pessoa, calcule o imc e mostre seu status. <18.5 = abaixo do peso, entre 18.5 e 25 = peso ideal, 25 até 30: sobrepeso, 30 até 40 obesidade. Acima de 40 obesidade mórbida

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if imc <18.5:
    print('Abaixo do Peso')
elif imc >18.5 and imc <25:
    print('Peso ideal')
elif imc >=25 and imc <30:
    print('Sobrepeso')
elif imc >=30 and imc<40:
    print('Obesidade')
elif imc >=40:
    print('Obesidade Mórbida')
