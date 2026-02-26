# Programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#a- Quantas vezes apareceu o valor 9. b-Em que posição digitado o primeiro valor 3. c- quais foram os números pares.

tupla = (int(input('Digite um número: ')), 
         int(input('Digite outro número: ')), 
         int(input('Digite mais um número: ')), 
         int(input('Digite o último número: ')))

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu pela primeira vez na {tupla.index(3)+1}° posição.')    
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
cont = 0
for c in range(0,len(tupla)):
    if tupla[c] %2==0:
        cont +=1
resp = 'Os valores pares digitados foram' if cont>1 else 'O valor par digitado foi'
if cont != 0:
    print(resp, end=' ')
    for c in range(0,len(tupla)):
        if tupla[c] %2==0:
            print(tupla[c], end=' ')
else:
    print('Nenhum número par foi digitado')




        
