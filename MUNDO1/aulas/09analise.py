#Manipulando Texto ANÁLISE

frase = 'Curso em Vídeo Python'

print(frase[9]) #Dessa forma o python vai printar o indíce 9
 
print(frase[9:13]) # Vai printar do indíce 9 até o 12

print(frase[9:21:2]) # Vai printar do indíce 9 até o 20 num intervalo de 2

print(frase[:5]) # Vai do início até o indíce 4

print(frase[15:]) # Vai do indíce 15 até o final

print(frase[9::3]) # Vai do 9 até o final pulando de 3 em 3

print(len(frase)) # len informa o tamanho da string

print(frase.count('o', 0, 13)) # informa quantas vezes aparece a letra "o". Usando o segundo e terceiro parâmetro, da para escolher um range para fazer essa pesquisa

print(frase.find('deo')) #Informa quantas vezes encontrou 'deo', mostrando aonde começou 'deo'

print(frase.find('Android')) # Quando não encontrou retorna -1

print('Curso' in frase) #Procura a palavra dentro da string