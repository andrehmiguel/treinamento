#13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:


altura = float(input("Insira sua altura em metros para calcular seu peso ideal: " ))
peso_masc = (72.7 * altura) - 58
peso_fem = (62.1 * altura) - 44.7
print(f"Considerando a altura de {altura:.02f}m, o peso ideal para homens é de {peso_masc:.02f}Kg. e para mulheres de {peso_fem:.02f}Kg.")