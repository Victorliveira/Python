# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado

import requests

try:
    r = requests.get('https://pudim.com.br')
    if r.status_code == 200:
        print('Foi possível acessar o site com sucesso')
    elif r.status_code == 404:
        print('A página não foi encontrada')
    else:
        print(f'O site apresentou erro.\n Status Code:{r.status_code}')
except:
    print('O site está fora do ar')
finally:
    print('Volte Sempre!')


