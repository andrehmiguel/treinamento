# 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a
# soma dos quadrados dos elementos do vetor.

a = []

for x in range(10):
    a.append(int(input(f'Informe o número {x + 1}: ')))

soma_quad = 0

for x in a:
    soma_quad += (x * x)

print(f'A soma dos quadrados dos números inseridos é = {soma_quad}')