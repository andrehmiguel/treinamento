# 5. Faça um programa com uma função chamada soma_imposto. A função possui dois
# parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
# função “altera” o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    return(1 + taxa_imposto / 100) * custo

t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo antes do imposto: '))
print(f'Valor com imposto: {soma_imposto(t,c)}')
