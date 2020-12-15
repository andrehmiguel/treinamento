# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# ========================================================
#               |Até 5 Kg           |Acima de 5 Kg
# Morango       |R$ 2,50 por Kg     |R$ 2,20 por Kg
# Maçã          |R$ 1,80 por Kg     |R$ 1,50 por Kg
# =========================================================
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
# quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo
# cliente.

morango = float(input('Digite a quantidade (Kg) de morangos: '))
maca = float(input('Digite a quantidade de (Kg) de maçãs: '))

if morango <= 5:
    preco_mo = 2.50 * morango
else:
    preco_mo = 2.20 * morango

if maca <= 5:
    preco_ma = 1.80 * maca
else:
    preco_ma = 1.50 * maca

preco = preco_ma + preco_mo

if preco > 25 or (morango + maca) > 8:
    desconto = (preco * 10) / 100
    preco = preco - desconto

print(f'Valor da compra: R$ {preco:.2f}')