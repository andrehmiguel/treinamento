# 11. Faça um programa que receba dois números inteiros e gere os números inteiros que
# estão no intervalo compreendido por eles.


num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

for x in range(num1, num2 + 1):
    print(x)
