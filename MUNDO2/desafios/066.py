# Programa que leia vários numeros inteiros. O programa só vai parar quando o usuários digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles

n = cont = s = 0
while True:
    n=int(input('Digite um valor (999 para parar): '))
    if n ==999:
        break
    cont+=1
    s+=n
print(f'A soma dos {cont} números é igual a {s}')
