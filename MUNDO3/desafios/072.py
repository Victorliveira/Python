# Programa que tenha uma tupla totalmente preenchida comuma contagem por extenso, de zero até vinte.
# O Programa deverá ler um num pelo teclado (0-20) e mostrálo por extenso.

num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

numesc = int(input('Digite um número entre 0 e 20: '))
while numesc >20 or numesc <0:
    print('Operação inválida, digite novamente! ')
    numesc = int(input('Digite um númetro entre 0 e 20: '))

print(f'Você digitou o número {num[numesc]}') 