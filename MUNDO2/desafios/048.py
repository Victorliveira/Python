# Programa que calcule e soma entre todos os números impares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500
soma = 0
contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        contador += 1
        soma += c
print(f'A soma dos {contador} números é igual a {soma}')