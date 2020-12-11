# 32. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
# agora possui uma loja de conveniências. Faça um programa que implemente uma
# caixa registradora rudimentar. O programa deverá receber um número desconhecido
# de valores referentes aos preços das mercadorias. Um valor zero deve ser
# informado pelo operador para indicar o final da compra. O programa deve então
# mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser
# conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00

while True:
    precos_produtos = []
    preco_produto = True
    n_produto = 1

    while preco_produto != 0:
        print("Produto n° ", n_produto)
        preco_produto = float(input("Digite o preço do produto: "))
        precos_produtos.append(preco_produto)
        n_produto += 1

    print("Total: ", sum(precos_produtos))
    dinheiro = float(input("Valor recebido: "))

    while dinheiro < sum(precos_produtos):
        dinheiro = float(input("Digite a quantida que irá pagar[maior que o total da compra] : "))

    print("Dinheiro: R$", dinheiro)
    print("Troco: R$", dinheiro - sum(precos_produtos))
    print('\n')
    print('--**--'*10)
    print('\n')