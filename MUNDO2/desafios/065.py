# Programa que leia vários num int. No final da execução, mostre a média entre todos os valores, qual foi os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer continuar a digitar valores.


continuar = 's'
numaior = numenor = contm = conts = 0


while continuar in('Ss'):
    num = int(input('Informe um número: '))     
    contm += 1
    conts += num
    if numaior == 0 and numenor == 0:
        numaior = numenor = num
    if numaior < num:
        numaior = num
    elif numenor > num:
        numenor = num    
    continuar = input('Deseja continuar? [S/N] ').strip()[0]
    while continuar not in('SsNn'):
        print('Escolha inválida, favor digite novamente')
        continuar = input('Deseja continuar? [S/N] ').strip()[0]
print(f'A média dos {contm} valores é igual a {conts / contm:.2f}')
print(f'O maior valor foi {numaior} e o menor foi {numenor}')



    