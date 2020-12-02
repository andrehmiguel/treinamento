#12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Insira sua altura em metros para calcular seu peso ideal: " ))
peso_ideal = (72.7 * altura) - 58
print(f"O seu peso ideal é de {peso_ideal:.02f} Kg.")