#Programa onde o usuário possa digitar 7 valores num e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. 

dados = [[],[]]
for v in range(1,8):
    num = int(input(f'Digite {v}° valor : '))
    if num %2 ==0:
        dados[0].append(num)
    else:
        dados[1].append(num)

print(f'Os valores pares digitados foram: ', sorted(dados[0]) )
print(f'Os valores ímpares digitados foram: ', sorted(dados[1]))