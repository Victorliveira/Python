#Programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - qtde de notas - maior nota - menor nota - média da turma - situação (opcional).
# adicionar docstring

def notas(*nota, sit=False):
    """
    -> Função que recebe n notas e informa, total de notas, maior nota, menor nota, média de nota e a situação total(opcional)
    :nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: Se sit for igual a True, a função apresenta a situação das notas
    :return: dicionário com várias informações sobre a situação da turma
    """
    print('-'*20)
    dic = dict()
    med = sum(nota)/len(nota)

    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['média'] = med
    if sit:
        if med >= 7:
            dic['situação'] = 'BOA'
        elif med >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic

#Programa Principal
resp = notas(5.5,9.5,10,6.5, sit=True)
print(resp)

help(notas)
