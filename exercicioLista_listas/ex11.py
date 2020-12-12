# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vet1 = []
vet2 = []
vet3 = []
vet4 = []

print('Informe os valores do primeiro vetor')
for x in range(10):
    vet1.append(int(input(f'Informe o número {x + 1}: ')))

print('\nInforme os valores do segundo vetor')
for x in range(10):
    vet2.append(int(input(f'Informe o número {x + 1}: ')))

print('\nInforme os valores do terceiro vetor')
for x in range(10):
    vet3.append(int(input(f'Informe o número {x+ 1}: ')))

for x in range(10):
    vet4.append(vet1[x])
    vet4.append(vet2[x])
    vet4.append(vet3[x])

print(vet4)