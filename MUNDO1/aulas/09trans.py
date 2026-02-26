#Manipulando Texto TRANSFORMAÇÃO

frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android')) # Substitui python por android

print(frase.upper()) # Transforma a str em maiusculo
print(frase.lower()) # Transforma a str em minusculo
print(frase.capitalize()) # Transforma os caracteres em minusculo e deixa a primeira em maisculo. Capitalizado

print(frase.title()) # Deixa todas as palavras com a inicial em maiusculo

frase2 = '   Aprenda Python  ' 

print(frase2.strip()) # Remove todos os espaços inuteis
print(frase2.rstrip()) # Remove somente os espaços a direita
print(frase2.lstrip()) # Remove somente os espaços a esquerda

