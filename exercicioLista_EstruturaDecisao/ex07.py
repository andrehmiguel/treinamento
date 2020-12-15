# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

lista = []
maior = 0
menor = 0

for x in range(3):
    lista.append(int(input(f'Digite o {x + 1}º número: ')))
    if x == 0:
        maior = menor = lista[x]
    elif lista[x] > maior:
        maior = lista[x]
    elif lista[x] < menor:
        menor = lista[x]

print(f'Os números inseridos foram: {lista}')
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')