# Programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa te voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

from datetime import datetime



def voto(idade):
    """
    -> Função que retorna se a pessoa tem o voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
    :param idade: idade da pessoa
    """
    if idade <= 15:
        return 'VOTO NEGADO'
    elif idade <=16 or idade >= 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'
    

help(voto)

nasc = int(input('Em que ano você nasceu? '))
idade = datetime.now().year - nasc 
print(f'Com {idade} anos: {voto(idade)}.')