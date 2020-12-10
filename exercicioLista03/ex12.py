# 12. Altere o programa anterior para mostrar no final a soma dos números.

lista = []
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

for x in range(num1, num2 + 1):
    print(x)
    lista.append(x)

print(list(range(num1, num2 + 1)))
print(f'A soma dos números é {sum(lista)}')
