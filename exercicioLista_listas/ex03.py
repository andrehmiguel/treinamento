# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista_notas = []
media = 0

print('Informe 4 notas para verificar a média')
for x in range(4):
    lista_notas.append(float(input(f'Nota {x + 1}: ')))
    media += lista_notas[x]

media = media / len(lista_notas)
print(f'Notas: {lista_notas}')
print(f'Média: {media}')