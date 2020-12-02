#06 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área e perímetro.

import math

raio = float(input("Insira o valor do Raio para calcular a área e perímetro de um círculo: "))
perimetro = 2 * math.pi * raio
area = math.pi * (raio ** 2)
print("Um círculo com raio de", raio, ", possui perímetro de", perimetro, "e área de ", area, ".")