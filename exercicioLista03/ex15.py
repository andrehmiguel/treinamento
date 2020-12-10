#15. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
# números pares e a quantidade de números ímpares.

lista = []
for x in range(1,11):
    lista.append(int(input(f'Insira o número {x}: ')))


par = 0
impar = 0
for x in lista:
    if x % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1


print(lista)
print(f'quantos pares: {par}')
print(f'quantos impares: {impar}')
