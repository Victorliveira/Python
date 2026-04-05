# programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário posso mostrar as notas da cada aluno individualmente

nome_nota= []
dados = []
print('Cadastro de Alunos')

while True:
    nome_nota.append(input('Nome: '))
    nome_nota.append(int(input('Nota 1: ')))
    nome_nota.append(int(input('Nota 2: ')))
    dados.append(nome_nota[:])
    nome_nota.clear()
    parar = str(input('Deseja continuar? [S/N] ')).upper()
    if parar not in ('SN'):
        print('Operação Incorreta! Digite novamente.')
        parar = str(input('Deseja continuar? [S/N] ')).upper()
    if parar == 'N':
        break

# Mostra o nome e média de todos alunos cadastrados
for pos, v in enumerate(dados):
    media = (dados[pos][1] + dados[pos][2])/2
    print()
    print('='*20)
    print(f'Nome: {dados[pos][0]}')
    print(f'Id Aluno: {pos}')
    print(f'Média: {media}')


while True:
    esc = int(input('\nNotas Detalhadas [1]\nSair [2]\n'))
    if esc not in (1,2):
        print('Operação Incorreta! Digite novamente.')
        esc = int(input(''))
    if esc == 1:
        rep = 'S'
        while rep == 'S':
            id = int(input('Informe o ID do Aluno: '))
            print(f'\nNome: {dados[id][0]}')
            print(f'Nota 1: {dados[id][1]}')
            print(f'Nota 2: {dados[id][2]}')
            rep = str(input('Deseja ver outras notas? [S/N]: ')).upper()
            if rep not in ('SN'):
                print('Operação Incorreta! Digite novamente.')
                rep = str(input('Deseja ver outras notas? [S/N]: ')).upper()
    break

print('PROGRAMA FINALIZADO')