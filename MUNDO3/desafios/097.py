# Programa que tenha uma função chamada escreva(), que receba um texto qlq como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    lan = int(len(msg)+4)
    print('~'*lan)
    print(f'{msg:^{lan}}')
    print('~'*lan)



escreva('Olá mundo')

escreva('Victor Souza')

escreva('Python')