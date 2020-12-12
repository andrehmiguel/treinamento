# 16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
# vendedores com base em comissões. O vendedor recebe $200 por semana mais 9
# por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
# teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de
# $3000, ou seja, um total de $470. Escreva um programa (usando um array de
# contadores) que determine quantos vendedores receberam salários nos seguintes
# intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante


salario_b = 200
vendedores = [0,0,0,0,0,0,0,0,0]

for x in range(0,10):
    valor_venda = float(input('Informe o valor das vendas do vendedor: '))
    salario = valor_venda * 0.09 + salario_b
    ind = int(salario / 100) - 1
    if (x > 9):
        x = 9
    elif (x < 1):
        x = 1
    print(x)
    vendedores[x - 1] += 1
