# Programa que tenha a função leiaint(), q vai funcionar de forma semelhante à função input(), só q fazerndo  a validação para aceitar apenas um valor numérico

def leiaInt(leia):
    """
    -> faz um input manual, guardando somente se for número inteiro
    :param leia: input desejado 
    """
    teste = input(leia)
    while not teste.isdigit():
        print('ERRO! Digite um número inteiro válido.')
        teste = input(leia)
    return teste

#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')