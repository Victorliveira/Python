#Programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Em que cidade você nasceu? ').strip()

upper = cidade.upper()
split = upper.split()


print('SANTO' in split[0])