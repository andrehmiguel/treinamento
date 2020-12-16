# 1. Faça um programa para imprimir:
# 1
# 2 2
# 3 3 3
# .....
# n n n n n n ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima
# até a n-ésima linha.

def numero(n):
    for x in range(n):
        x += 1
        print(str(x) * x)

n = int(input('Digite um número: '))
numero(n)