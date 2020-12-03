#16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#lata 18L
#1L -> 3m2
#1 lata -> 80 reais
#quantas latas e preço?

import math as mt


m2 = float(input("Informe a quantidade de metros quadrados da área a ser pintada: "))
litros = m2 / 3
#latas = litros / 18
#custo = latas * 80

if litros <= 18:
    print(f'Para pintar {m2}m², você deve comprar 1 lata de tinta, ao custo de R$ 80,00.')
else:
    latas = mt.ceil(litros/18)
    #arredondando a divisão para cima
    custo = latas * 80

    print(f'Para pintar {m2}m², você deve comprar {latas} latas, ao custo de R$ {custo:.02f}')





