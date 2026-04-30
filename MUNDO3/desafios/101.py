# Programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa te voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições


def voto(ano):
    """
    -> Função que retorna se a pessoa tem o voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
    :param idade: idade da pessoa
    """
    from datetime import datetime
    idade = datetime.now().year - ano 
    if idade <= 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade <18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    

#Programa Principal
print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))