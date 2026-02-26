# programa que calcula o valor a saer pago por um produto, considerando o seu preço normal e condição de pagamento. a vista dinheiro/cheque:10% de desconto, a vista no cartão:5% de desconto. em até 2x no cartão:preço normal. 3x ou mais 20% de juros

valor = float(input('Informe o valor do produto: '))
print('Métodos de pagamento\n[1] à vista no dinheiro/cheque\n[2] à vista no Cartão\n[3] 2x no cartão\n[4] 3x no cartão')
metodo = input('Informe o método de pagamento:')



if metodo == '1':
    valord = valor - (valor*0.1) 
    print(f'O valor do produto sendo pago à vista no dinheiro é {valord}')
elif metodo == '2':
    valorc = valor - (valor*0.05)
    print(f'O valor do produto sendo pago à vista no cartão é {valorc}')
elif metodo =='3':
    print(f'O valor do produto sendo pago 2x no cartão é {valor}')
elif metodo =='4':
    valorc = valor + (valor*0.2)
    parcelas = int(input('Quantas parcelas?'))
    print(f'Sua compra será parcelada em {parcelas} parcelas de R${valorc/parcelas:.2f} COM JUROS.')
    print(f'O valor do produto sendo pago em {parcelas} vezes ou mais no cartão é {valorc:.2f}')