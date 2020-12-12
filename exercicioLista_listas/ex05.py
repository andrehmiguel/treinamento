# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

lista_num = []
par = []
impar = []
print ('Informe 20 números inteiros')
for x in range(20):
    lista_num.append(int(input(f'Informe o {x + 1}º número: ')))
    num = lista_num[x]
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(lista_num)
print(par)
print(impar)