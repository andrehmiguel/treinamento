# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
# multiplicação e os números.

num = []

for x in range (0,4):
    num.append(int(input(f'Informe o {x + 1}º número: ')))

soma = 0
mult = 1
for x in num:
    soma += x
    mult *= x

print(num)
print(soma)
print(mult)