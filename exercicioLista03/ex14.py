# 14. Faça um programa que peça dois números, base e expoente, calcule e mostre o
# primeiro número elevado ao segundo número. Não utilize a função de potência da
# linguagem.


base = int(input('Insira o número base: '))
expo = int(input('Insira o número expoente: '))

potencia = 1

for x in range(expo):
    potencia = potencia * base
    x = x + 1


print(potencia)