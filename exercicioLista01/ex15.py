#15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
"""
- Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Líquido : R$"""


ganhos_hora = int(input("Informe quanto você ganha por hora trabalhada: "))
horas_trab = int(input("Informe quantas horas você trabalhou no mês: "))

bruto = ganhos_hora * horas_trab
ir = 0.11 * bruto
inss = 0.08 * bruto
sindicato = 0.05 * bruto
liquido = bruto - ir - inss - sindicato

print(f'Salário bruto: R${bruto:.02f}')
print(f'Imposto de renda: R${ir:.02f}')
print(f'INSS: R${inss:.02f}')
print(f'Sindicato: R${sindicato:.02f}')
print(f'Salário líquido: R${liquido:.02f}')




