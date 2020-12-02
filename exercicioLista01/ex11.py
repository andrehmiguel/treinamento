#11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

num1 = int(input("Insira um número inteiro: "))
num2 = int(input("Insira outro número inteiro: "))
num3 = float(input("Insira um número real: "))

calc1 = (num1 * 2) * (num2 / 2)
#o produto do dobro do primeiro com metade do segundo
calc2 = (num1 * 3) + num3
#a soma do triplo do primeiro com o terceiro.
calc3 = num3 ** 3
#o terceiro elevado ao cubo

print("O produto do dobro do primeiro com metade do segundo: ", calc1)
print("A soma do triplo do primeiro com o terceiro: ", calc2)
print(f'O terceiro elevado ao cubo é: {calc3:.02f}')