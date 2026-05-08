# Reescreva a função leiaInt() que foi feito no ex104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma funcção leia Float() com a msm funcionalidade 

def leiaInt(leia):
    """
    -> faz um input manual, guardando somente se for número inteiro
    :param leia: input desejado 
    """
    while True:
        try:                
            teste = int(input(leia))
        except (ValueError, TypeError):
            print('Tivemos um erro com o tipo de valor digitado')
        except KeyboardInterrupt:
            print('O usuário decidiu não informar o valor')
            teste = 0
            return teste
            break
        else:
            return teste
            break

def leiaFloat(leia):
    """
    -> faz um input manual, guardando somente se for número float
    :param leia: input desejado 
    """
    while True:
        try:    
            teste = float(str(input(leia)).replace(',','.').strip())
            testev = float(teste)
        except (ValueError, TypeError):
            print('Tivemos um problema com o valor digitado')
        except KeyboardInterrupt:
            print('O usuário decidiu não informar um valor!')
            teste= 0
            return teste
            break
        else:
            return teste
            break

print(f'O valor inteiro digitado foi {leiaInt("Digite um Inteiro: ")} e o real foi {leiaFloat("Digite um Real: ")}')