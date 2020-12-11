# 35. Os números primos possuem várias aplicações dentro da Computação, por exemplo
# na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele
# mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
# um número primo.

numero = int(input("Digite um número: "))

if numero % 2 != 0 or numero == 2:
    print(f"{numero} é um número primo.")
else:
    print(f'{numero} não é número primo.')