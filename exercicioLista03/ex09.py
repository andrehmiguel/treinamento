# 09. Faça um programa que leia 5 números e informe a soma e a média dos números.


lista = []
for num in range(1, 6):
    lista.append(int(input(f'Digite o número {num}: ')))

soma = sum(lista)
media = (sum(lista)) / len(lista)
print(f'Soma dos números inseridos: {soma}')
print(f'Média dos números inseridos: {media}')