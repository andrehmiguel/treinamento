#04 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Entre com as notas de cada bimestre para calcular a média.")
bim1 = float(input("Insina a nota do 1º bimestre: "))
bim2 = float(input("Insina a nota do 2º bimestre: "))
bim3 = float(input("Insina a nota do 3º bimestre: "))
bim4 = float(input("Insina a nota do 4º bimestre: "))
media = (bim1 + bim2 + bim3 + bim4) / 4
print("A média final é ", media,".")
