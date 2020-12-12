# 10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.

vet1 = []
vet2 = []
vet3 = []

print('Informe os valores do primeiro vetor')
for x in range(10):
    vet1.append(int(input(f'Informe o número {x + 1}: ')))

print('\nInforme os valores do segundo vetor')
for x in range(10):
    vet2.append(int(input(f'Informe o número {x + 1}: ')))

for x in range(10):
    vet3.append(vet1[x])
    vet3.append(vet2[x])

print(vet3)