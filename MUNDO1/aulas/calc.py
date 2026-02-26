print('INICIANDO CALCULADORA')
iniciar = 1
while iniciar == 1:
    num1 = float(input('Escolha o primeiro número : '))
    num2 = float(input('Escolha o segundo número : '))

    print('Adição = +')
    print('Subtração = -')
    print('Multiplicação = *')
    print('Divisão = / ')

    operador = input('Escolha o operador: ')

    if operador == "+":
        soma = num1 + num2
        print(f'A soma dos números é igual a {soma}')
    elif operador == "-":
        sub = num1 - num2
        print(f'A subtração dos números é igual a {sub}')
    elif operador == '*':
        mult = num1 * num2
        print(f'A muliplicação dos números é igual a {mult}')
    elif operador =='/':
        div = num1 / num2 
        print(f'A divisão dos números é igual a {div}')
    else:
        print('Operador desconhecido')
    dnv = input('Deseja fazer outro cálculo? Se sim, digite 1, se não digite 0: ')
    
    if dnv == '0':
        iniciar = 0
        print('ENCERRANDO CALCULADORA')
        
    

