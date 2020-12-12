# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem
# inversa.

lista = []
print('Informe 10 números inteiros')
for x in range(10):
    lista.append(input(f'Número {x + 1}: '))

lista.reverse()
print(lista)
