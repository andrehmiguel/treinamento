#08 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


ganha_hora = int(input("Quanto você ganha por hora? "))
hora_trab = int(input("Quantas horas você trabalhou esse mês? "))
salario = ganha_hora * hora_trab
print("Seu salário correspondente ao mês é de R$", salario,".")