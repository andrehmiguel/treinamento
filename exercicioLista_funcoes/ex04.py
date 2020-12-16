# 4. Faça um programa, com uma função que necessite de um argumento. A função
# retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu
# argumento for zero ou negativo.

def pn(n):
    if n > 0:
        print('P')
    elif n == 0:
        print('Nulo')
    else:
        print('N')
n = int(input('Digite um número: '))
print(f'Esse número é ', end = ' ')
pn(n)

