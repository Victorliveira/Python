# Mini-sistema que utilize o interactive help do pyuthon. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 'FIM', o programa encerrará.
from time import sleep

def escreva(msg,cori, corf = "\033[0m"):
    """
    -> Apresenta uma mensagem formatada e com cor
    :param msg: Mensagem para ser apresentada
    :param cori: Cor de ínicio
    :param corf: Cor final
    """
    lan = int(len(msg)+4)
    print(f'{cori}~'*lan)
    print(f'{msg:^{lan}}')
    print(f'~'*lan, corf)

def ajuda():
    """
    -> Mini sitema que auxilia o usuário com as funções/bibliotecas do python
    """
    while True:
        escreva('SISTEMA DE AJUDA PYHELP', "\033[42m")
        func = input(f'Função ou Bibilioteca -> ')

        if func.upper() in ('FIM'):
            escreva('ATÉ LOGO', '\033[41m' )
            break

        escreva(f'Acessando o manual do comando "{func}"',"\033[44m" )
        sleep(0.7)

        help(func)   

ajuda()