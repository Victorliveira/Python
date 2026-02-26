# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra qual ele disser que quer mostrar 0 termos

print('='*30)
print('GERADOR DE PA')
print('='*30)
prim = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão: '))
n = 1
termo = prim
termo_qte = 10
term_ad = 1

while n <= termo_qte  :
    if n < termo_qte:
        print(f'{termo} -> ', end='')
    
    if n == termo_qte:
        print(f'{termo} -> PAUSA', end='')
        term_ad = int(input('\nDeseja ver mais quantos termos? '))
        termo_qte += term_ad
    termo += raz
    n += 1
print(f'Progressão finalizada com {n} termos mostrados.')