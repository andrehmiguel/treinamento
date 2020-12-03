#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# 1L para cada 6m²
#comprar apenas latas de 18 litros (R$ 80,00;
#comprar apenas galões de 3,6 litros (R$ 25,00);
#misturar latas e galões, de forma que o desperdício de tinta seja menor.

import math

m2 = float(input("Informe a quantidade de metros quadrados da área a ser pintada: "))
litros = m2 / 6
latas = litros // 18 + 1
galoes = litros // 3.6 + 1
custo_latas = latas * 80
custo_galoes = galoes * 25
mistura = (litros // 18) * 80 + ((litros % 18) // 3.6 + 1) * 25
"""Quantidade de latas que serão usadas * o custo
O que sobrar da divisão por 18 então, é calculado em função da quantidade de galões então * o custo"""
misturalata = litros // 18
misturagalao = ((litros % 18) // 3.6 + 1)


print(f'Considerando a quantidade de {m2}m², haveria um custo de R${custo_latas:.02f} por {latas} latas.')
print(f'Considerando a quantidade de {m2}m², haveria um custo de R${custo_galoes:.02f} por {galoes} latas.')
print(f'Considerando a quantidade de {m2}m², haveria um custo de R${mistura:.02f}. por {misturalata} latas e {misturagalao} galões.')




