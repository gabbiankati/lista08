    # 3) Desenvolva uma função que receba um número inteiro e positivo N e retorne a soma dos N
    # números inteiros existentes entre o número 1 e esse número.

def soma_numeros(N):
    soma = 0
    for i in range(1, N+1):
        soma += i
    return soma