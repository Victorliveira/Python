# Programa que pergunta a quantidade de km percorridos por um carro alugado, a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))

valor = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${valor:.2f}')
