# 3. Faça um programa, com uma função que necessite de três argumentos, e que
# forneça a soma desses três argumentos.

def soma(a, b, c):
    soma = a + b + c
    return soma

a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

print(f'Soma = {soma(a, b, c)}')
