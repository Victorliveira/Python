#Tratamento de erros e exceções 

print()

try:
    # Testa o código
    a= int(input('Numerador: '))
    b= int(input('Divisor: '))
    r = a/b

except (ValueError,TypeError): # Se acontecer o erro especifico gera o código abaixo
    print(f'Tivemos um problema com os tipos de dados')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por 0')
except Exception as erro: # Validar o tipo de erro que aconteceu
    # Resultado caso aconteça problema
    print(f'Problema encontrado foi {erro.__class__}')
else:
    # Resultado caso n aconteça problema
    print(f'O resultado é {r:.1f}')
finally:
    # Gera esse código independente de erro ou não
    print('Volte sempre! Muito obrigado!')



