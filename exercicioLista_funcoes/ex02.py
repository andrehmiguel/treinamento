# 2. Faça um programa para imprimir:
# 1
# 1 2
# 1 2 3
# .....
# 1 2 3 ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima
# até a n-ésima linha.


n = int(input('Digite um número: '))
def lista(n):
    for x in range(n + 1):
        new = []
        for y in range(x):
            new.append(str(y + 1))
        print(' '.join(new))
lista(n)
