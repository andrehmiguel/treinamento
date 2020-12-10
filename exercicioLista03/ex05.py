# 05 Altere o programa anterior permitindo ao usuário informar as populações e as taxas
# de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = int(input('População A: '))
while a <= 0:
    a = int(input('Inválido. Insira um tamanho maior que 0 para a população do país A: '))
a_taxa = float(input('Informe a taxa de crescimento do país A'))

b = int(input('População B: '))
while b <= 0:
    b = int(input('Inválido. Insira um tamanho maior que 0 para a população do país A: '))
b_taxa = float(input('Informe a taxa de crescimento do país B'))

ano = 0

while a <= b:
    a += a * (a_taxa / 100)
    b += b * (b_taxa / 100)
    ano += 1

print(f'A população do país A ultrapassará ou irá se igualar a população do país B em {ano} anos')

print(f'Ultrapassa no ano: {ano}')