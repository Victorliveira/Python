def leiaDinheiro(ler):
    teste = str(input(ler))
    while True:
        teste = teste.replace(',','.')
        teste = teste.strip()    
        if teste.count('.') <=1 and teste.replace('.','').isdigit():
            break
        else:
            print(f'ERRO: "{teste}" é um preço inválido!')
            teste = str(input(ler))

    return float(teste)
    
    