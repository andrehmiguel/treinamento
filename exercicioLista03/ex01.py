# 01. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
# válido.

nota = int(input('Insira uma nota de 1 a 10: '))

while (nota > 10) or (nota < 0):
    nota = int(input(f'A nota {nota} é inválida. Digite outra nota de 1 a 10: '))
else:
    print((f'A nota {nota} é válida!'))
