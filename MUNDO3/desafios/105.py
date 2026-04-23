#Programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - qtde de notas - maior nota - menor nota - média da turma - situação (opcional).
# adicionar docstring

def notas(*nota, sit=False):
    """
    -> Função que recebe n notas e informa, total de notas, maior nota, menor nota, média de nota e a situação total(opcional)
    :param sit: Se sit for igual a True, a função apresenta a situação das notas
    """
    print('-'*20)
    dic = dict()
    if not sit:
        dic = {'total' : len(nota),
            'maior': max(nota),
            'menor': min(nota),
            'média': (sum(nota)/len(nota))}
    else:
        med = sum(nota)/len(nota)
        if med >= 7:
            situ = 'BOA'
        elif med >= 5:
            situ = 'RAZOÁVEL'
        else:
            situ = 'RUIM'
        dic = {'total' : len(nota),
            'maior': max(nota),
            'menor': min(nota),
            'média': med ,
            'situação': situ}
    return dic

#Programa Principal
resp = notas(5.5,9.5,10,6.5, sit=True)
print(resp)

help(notas)
