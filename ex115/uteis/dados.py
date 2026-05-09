from time import sleep

dados = dict()
grupo = list()
numero = 0

def mostramsg(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)

def menu():
    sleep(0.3)
    mostramsg('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistema')
    print('-'*40)
    option()

def validaint(txt, max=99, vmax = False):
    num = 0
    if vmax:
        while True:
            try:
                num = int(input(f'{txt}: '))
                while num >= max:
                    print('Erro, digite um número válido!')
                    num = int(input(f'{txt}: '))
            except (ValueError, TypeError):
                print('Erro, digite um número válido!')
            else:
                break
    elif not vmax:
        while True:
            try:
                num = int(input(f'{txt}: '))
            except (TypeError,ValueError):
                print('Erro, digite um número válido!')
            else:
                break
    return num

def option():            
    numoption = validaint('Sua Opção', 4, True)
    
    if numoption == 1:
        ver()
    elif numoption == 2:
        cadastrar()
    else:
        sleep(0.5)
        print('PROGRAMA ENCERRADO, VOLTE SEMPRE')
    
def cadastrar():
    sleep(0.5)
    mostramsg('NOVO CADASTRO')
    sleep(0.3)
    dados['Nome']= str(input('Nome: ')).capitalize().strip()
    dados['Idade']= validaint('Idade', vmax=False)
    grupo.append(dados.copy())
    menu()

def ver():
    mostramsg('PESSOAS CADASTRADAS')
    for pos,v in enumerate(grupo):
        print(f'{v["Nome"]:<20} {v["Idade"]:>4} anos')
    menu()

