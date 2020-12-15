# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o
# número de litros vendidos, o tipo de combustível (codificado da seguinte
# forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do
# álcool é R$ 1,90.

comb = input('Insira o tipo de combustível -> A - Álcool | G - Gasolina: ').lower().strip()
litros = float(input('Qual a quantidade de litros: '))

if comb == 'a':
    preco = 1.90
    if litros <= 20:
        desconto = 3
    else:
        desconto = 5
elif comb == 'g':
    preco = 2.50
    if litros <= 20:
        desconto = 4
    else:
        desconto = 6

custo = (litros * preco)
custo_final = custo - ((custo * desconto) / 100)
print(f'Preço total sem desconto: R$ {custo:.2f}')
print(f'Preço total com desconto: R$ {custo_final:.2f}')








