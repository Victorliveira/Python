# Programa que tenha uma função fatorial() que receba doi parâmetros: o primeiro que indique o num a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

from time import sleep

def fatorial(num,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    c = num
    while c >= 1:
        if show == True:
            if c >1:
                sleep(0.2)
                print(c, end=' x ', flush=True)
            else:
                sleep(0.2)
                print(c, end=' = ', flush=True)
        c -= 1
        if c >0:
            num *= c
    return num
        
print(fatorial(5, True))

