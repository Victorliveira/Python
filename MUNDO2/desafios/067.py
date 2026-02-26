#Programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuários. O programa será interrompido quando o número for negativo.

n=0

while True:
    n = int(input('Informe um número para ver sua tabuada: '))
    print('-'*20)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Programa de Tabuada encerrado!')
        
