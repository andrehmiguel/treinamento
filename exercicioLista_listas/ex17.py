# 17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado
# do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um
# programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
# depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado
# quando não for informado o nome do atleta. A saída do programa deve ser conforme o
# exemplo abaixo:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

texto = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
nome = ' '
atletas = {}

while (nome != ''):
    nome = input('Atleta: ')
    if (nome != ''):
        saltos = []
        for i in texto:
            saltos.append(float(input(f'Salto: {i}')))
        atletas[nome] = saltos

for (nome, saltos) in atletas.items():
    print(f'Atleta: {nome}')
    print(f'Saltos: {saltos}')
    somasaltos = 0.0
    for salto in saltos:
        somasaltos += salto
    print(f'Média dos saltos é de {somasaltos / float(len(texto))}')