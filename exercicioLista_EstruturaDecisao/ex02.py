# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou
# negativo.


n = float(input('Insira um número: '))

if n < 0:
    print(f'O valor {n} que você digitou é negativo.')
else:
    print(f'O valor {n} que você digitou é positivo.')