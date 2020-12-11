# 39. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
# dobro do percentual do ano anterior. Faça um programa que determine o
# salário atual deste funcionário.

salario = float(1000)
aumento = 1.5

for i in range(1996, 2018 + 1):
    aumento = aumento * 2
    salario_atual = salario + (salario * (aumento / 100))
    print("Salário do funcionário: ", i, " = ", salario_atual)