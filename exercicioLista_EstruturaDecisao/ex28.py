# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
# ===============================================
#               |Até 5 Kg        |Acima de 5 Kg
# File Duplo    |R$ 4,90 por Kg  |R$ 5,80 por Kg
# Alcatra       |R$ 5,90 por Kg  |R$ 6,80 por Kg
# Picanha       |R$ 6,90 por Kg  |R$ 7,80 por Kg
# ================================================
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos
# tipos de carne da promoção, porém não há limites para a quantidade de
# carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
# ainda um desconto de 5% sobre o total da compra. Escreva um programa
# que peça o tipo e a quantidade de carne comprada pelo usuário e gere um
# cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


carne = input('Digite uma opção de carne: (1) Filé Duplo / (2) Alcatra / (3) Picanha: ').strip()
kg = float(input('Digite a quantidade de carne em Kg: '))
cartao = input('Pagamento com cartão tabajara? (1) Sim / (2) Não: ')

if carne == '1':
    carne = 'Filé Duplo'
    if kg <= 5:
        preco = kg * 4.90
    else:
        preco = kg * 5.80

elif carne == '2':
    carne = 'Alcatra'
    if kg <= 5:
        preco = kg * 5.90
    else:
        preco = kg * 6.80

elif carne == '3':
    carne = 'Picanha'
    if kg <= 5:
        preco = kg * 6.90
    else:
        preco = kg * 7.80

if cartao == '1':
    cartao = 'SIM'
    desconto = (preco * 5) / 100
    precof = preco - desconto
elif cartao == '2':
    cartao = 'NÃO'
    desconto = 0
    precof = preco


print('=*=' * 15)
print(f'Tipo de carne....................{carne}')
print(f'Quantidade de carne..............KG {kg:.2f}')
print(f'Preco total......................R$ {preco:.2f}')
print(f'Cartão Tabajara..................{cartao}')
print(f'Valor do desconto................R$ {desconto:.2f}')
print(f'Valor a pagar....................R$ {precof:.2f}')


