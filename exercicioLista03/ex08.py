# 08. Faça um programa que leia 5 números e informe o maior número.

lista = []
for num in range (1, 6):
    lista.append(int(input(f'Digite o número {num}: ')))

print(f'Você digitou os números: {lista} ')
print(f'O maior número é {max(lista)}')