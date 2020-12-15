# 6. Faça um Programa que leia três números e mostre o maior deles.

n1, n2, n3 = float(input("Insira o primeiro número: ")), float(input("Insira o segundo número: ")), float(input("Insira o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f'O maior valor é {n1}.')
elif n2 > n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior valor é {n3}')
