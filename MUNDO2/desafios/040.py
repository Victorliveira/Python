#Programa que le duas notas e e calcula sua média, mostrando uma mensagem no final de acordo com a média. <5 = reprovado, >5 e <6.9= recuperação, => 7 aprovado

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO')
elif media > 5 and media < 6.9:
    print('RECUPERAÇÃO')
elif media >= 6.9:
    print('APROVADO')
