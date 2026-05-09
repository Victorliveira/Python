from time import sleep

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
                return str(num)
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
    arquivo = open('dados.txt','a')
    sleep(0.5)
    mostramsg('NOVO CADASTRO')
    sleep(0.3)
    name = validanome('Nome')
    age = validaint('Idade', vmax=False)
    arquivo.write(f'{name:<5}\t; {age:>5} anos\n')
    arquivo.close()
    menu()

def ver():
    mostramsg('PESSOAS CADASTRADAS')
    arquivo = open('dados.txt','a+')
    arquivo.seek(0)
    for linha in arquivo:
        linha.split(';')
        print(linha.replace(';',''), end='')
    arquivo.close()
    menu()

def validanome(txt):
    while True:
        ok = True
        name = input(f'{txt}: ').capitalize().strip()
        if name == '':
            print('Erro, digite um nome válido')
            ok = False
        else:
            for c in name:
                if c.isnumeric():
                    print('Erro, digite um nome válido!')
                    ok = False
                    break
        if ok:
            break
    return str(name)