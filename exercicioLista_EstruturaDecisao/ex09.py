# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []
for x in range(3):
    lista.append(int(input(f'Insira o {x}º número: ')))
print(f'Aqui estão os números em ordem inversa: {lista[::-1]}')