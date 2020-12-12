# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
print('Informe 5 números inteiros')
for x in range(5):
    lista.append(input(f'Número {x + 1}: '))

print(lista)