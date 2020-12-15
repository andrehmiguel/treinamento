# 1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input(f'Insira o primeiro número: '))
n2 = float(input(f'Insura o segundo número: '))

if n1 > n2:
    print(f'O primeiro número >{n1}< é o maior.')
else:
    print(f'O segundo número >{n2}< é o maior.')