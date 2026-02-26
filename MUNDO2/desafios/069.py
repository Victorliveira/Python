#Programa que leia a idade e o sexo de várias pessoas. Cada pessoa cadastrada, o programa deverá perguntar se o usuários quer ou não continuar. No final, mostre:
#a - quantas pessoas tem mais de 18 anos. b- quantos homens foram cadastrados c-quantas mulheres tem menos de 20 anos

idade = conti = contm = contm20 = 0
sexo = seguir ='a'


while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in('MF'):
        print('Opção INVALIDA, digite novamente! ')
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if idade >18:
        conti+=1
    if sexo =='M':
        contm+=1
    if sexo == 'F' and idade <20:
        contm20+=1
    seguir = input('Quer continuar? [S/N]  ').strip().upper()[0]
    print('-'*25)
    while seguir not in ('SN'):
        print('Opção INVALIDA, digite novamente! ')
        seguir = input('Deseja cadastrar mais pessoas [S/N]? ').upper()
    if seguir == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {conti}')
homem = 'homem' if contm == 1 else 'homens'
print(f'Ao todo temos {contm} {homem} no sistema.')
mulher = 'mulher' if contm20 ==1 else 'mulheres'
print(f'E temos {contm20} {mulher} com menos de 20 anos')