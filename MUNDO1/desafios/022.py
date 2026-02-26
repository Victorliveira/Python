#programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letrias maiusculas; todas minusculas ; quantas letrar ao todo(sem considerar espaços) ; quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()

print(f'Esse é seu nome com todas as letras maiúsculas: {nome.upper()}')

print(f'Esse é seu nome com todas as letras minúsculas: {nome.lower()}')

letras = nome.split()
letrasjoin = ''.join(letras)

print(f'Seu nome tem {len(letrasjoin)} letras')

primeironome = nome.split()

print(f'Seu primeiro nome tem {len(primeironome[0])} letras')