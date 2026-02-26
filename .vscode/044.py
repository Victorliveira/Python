# programa que calcula o valor a saer pago por um produto, considerando o seu preço normal e condição de pagamento. a vista dinheiro/cheque:10% de desconto, a vista no cartão:5% de desconto. em até 2x no cartão:preço normal. 3x ou mais 20% de juros

valor = float(input('Informe o valor do produto: '))
print('Métodos de pagamento\nDinheiro/cheque\nCartao\n2xCartao\n3xcartao')
metodo = input('Informe o método de pagamento:')



if metodo == 'dinheiro':
    valord = (valor*0,1) - valor
    print('O valor do produto sendo pago à vista no dinheiro é ')