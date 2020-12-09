
# VARIÁVEIS INICIAIS
tipo_conta = input("Informe o tipo de tarifa a ser calculada: 1 - Residencial / 2 - Não residencial: ")
while (tipo_conta != '1') and (tipo_conta != '2'):
    tipo_conta = input('Opção inválida: 1 - Residencial / 2 - Não residencial: ')
consumo = int(input('Informe seu consumo em m³: '))
sistema = input('Informe situação do sistema: 1 - Convencional / 2 - Obra: ')
while (sistema != '1') and (sistema != '2'):
    sistema = input('Opção inválida: 1 - Convencional / 2 - Obra: ')

# RESIDENCIAL
if tipo_conta == "1":

    tipo_tarifa = input('Informe tipo da tarifa: 1 - Padrão / 2 - Social: ')
    while (tipo_tarifa != '1') and (tipo_tarifa != '2'):
        tipo_tarifa = input('Opção inválida: 1 - Padrão / 2 - Social: ')
    unidade = int(input('Informe a quantidade de unidades de consumo: '))
    consumo_unidade = consumo / unidade

    tarifa1 = 8.00
    tarifa2 = 4.00

    # RESIDÊNCIA TIPO PADRÃO
    if tipo_tarifa == "1":
        tarifa = tarifa1
        if (consumo_unidade <= 7):
            preco = (2.99 * consumo_unidade)
        elif (consumo_unidade > 7 and consumo_unidade <= 13):
            preco = (20.93 + (consumo_unidade - 7) * 3.59)
        elif (consumo_unidade > 13 and consumo_unidade <= 20):
            preco = (20.93 + 21.54 + (consumo_unidade - 13) * 7.10)
        elif (consumo_unidade > 20 and consumo_unidade <= 30):
            preco = (20.93 + 21.54 + 49.70 + (consumo_unidade - 20) * 10.66)
        elif (consumo_unidade > 30 and consumo_unidade <= 45):
            preco = (20.93 + 21.54 + 49.70 + 106.60 + (consumo_unidade - 30) * 17.05)
        elif consumo_unidade > 45:
            preco = (20.93 + 21.54 + 49.70 + 106.60 + 255.75 + (consumo_unidade - 45) * 23.87)

    # RESIDÊNCIA TIPO SOCIAL
    elif tipo_tarifa == "2":
        tarifa = tarifa2
        if (consumo_unidade <= 7):
            preco = (1.49 * consumo_unidade)
        elif (consumo_unidade > 7 and consumo_unidade <= 13):
            preco = (10.43 + (consumo_unidade - 7) * 1.79)
        elif (consumo_unidade > 13 and consumo_unidade <= 20):
            preco = (10.43 + 10.74 + (consumo_unidade - 13) * 3.55)
        elif (consumo_unidade > 20 and consumo_unidade <= 30):
            preco = (10.43 + 10.74 + 24.85 + (consumo_unidade - 20) * 5.33)
        elif (consumo_unidade > 30 and consumo_unidade <= 45):
            preco = (10.43 + 10.74 + 24.85 + 53.30 + (consumo_unidade - 30) * 17.05)
        elif consumo > 45:
            preco = (10.43 + 10.74 + 24.85 + 53.30 + 255.75 + (consumo_unidade - 45) * 23.87)

# NÃO RESIDENCIAL
elif tipo_conta == "2":

    tipo_tarifa = input('Informe tipo da tarifa: 1 - Comercial, Industrial ou Público / 2 - Paisagismo: ')
    while (tipo_tarifa != '1') and (tipo_tarifa != '2'):
        tipo_tarifa = input('Opção inválida: 1 - Comercial, Industrial ou Público / 2 - Paisagismo: ')
    unidade = 1
    consumo_unidade = consumo / unidade
    tarifa1 = 21.00
    tarifa2 = 31.50

    # COMERCIAL, INDUSTRIAL OU PÚBLICO
    if tipo_tarifa == "1":
        tarifa = tarifa1
        if (consumo_unidade <= 4):
            preco = (6.14 * consumo_unidade)
        elif (consumo_unidade > 4 and consumo_unidade <= 7):
            preco = (24.56 + (consumo_unidade - 4) * 7.68)
        elif (consumo_unidade > 7 and consumo_unidade <= 10):
            preco = (24.56 + 23.04 + (consumo_unidade - 7) * 9.98)
        elif (consumo_unidade > 10 and consumo_unidade <= 40):
            preco = (24.56 + 23.04 + 29.94 + (consumo_unidade - 10) * 12.48)
        elif consumo_unidade > 40:
            preco = (24.56 + 23.04 + 29.94 + 374.40 + (consumo_unidade - 40) * 14.97)

    # PAISAGISMO
    elif tipo_tarifa == "2":
        tarifa = tarifa2
        if (consumo_unidade <= 4):
            preco = (9.21 * consumo_unidade)
        elif (consumo_unidade > 4 and consumo_unidade <= 7):
            preco = (36.84 + (consumo_unidade - 4) * 11.52)
        elif (consumo_unidade > 7 and consumo_unidade <= 10):
            preco = (36.84 + 34.56 + (consumo_unidade - 7) * 14.97)
        elif (consumo_unidade > 10 and consumo_unidade <= 40):
            preco = (36.84 + 34.56 + 44.91 + (consumo_unidade - 10) * 18.72)
        elif consumo_unidade > 40:
            preco = (36.84 + 34.56 + 44.91 + 561.60 + (consumo_unidade - 40) * 22.46)

# PREÇO UNIDADE
# SISTEMA CONVENCIONAL
if sistema == '1':
    tarifa_var_agua = preco
    tarifa_var_esgoto = preco
    preco_unidade = (preco * 2) + (tarifa * 2)

# SISTEMA EM OBRA
elif sistema == '2':
    tarifa_var_agua = preco
    tarifa_var_esgoto = preco / 2
    preco_unidade = (preco + preco / 2) + (tarifa * 2)
    print('==*==' * 15)
    print('Imóvel em obra, tarifa variável de esgoto reduzida em 50%')

# PREÇO FATURA TOTAL
fatura = preco_unidade * unidade

# SAÍDA
# VALORES TOTAIS FIXOS E VARIÁVEIS
print('==*==' * 15)
print(f'Tarifa fixa água / esgoto por unidade:          |R$ {tarifa:.2f} / R$ {tarifa:.2f}')
print(f'Tarifa fixa total por unidade  :                |R$ {(tarifa + tarifa):.2f}')
print(f'Tarifa fixa total água / esgoto:                |R$ {(tarifa * unidade):.2f} / R$ {(tarifa * unidade):.2f}')
print(f'Tarifa fixa total:                              |R$ {(tarifa * unidade * 2):.2f}')

print('==*==' * 15)
print(f'Tarifa variável água / esgoto por unidade:      |R$ {tarifa_var_agua:.2f} / R$ {tarifa_var_esgoto:.2f}')
print(f'Tarifa variável total por unidade:              |R$: {(tarifa_var_agua + tarifa_var_esgoto):.2f}')
print(f'Tarifa variável total água / esgoto:            |R$: {(tarifa_var_agua * unidade):.2f} / R$ {(tarifa_var_esgoto * unidade):.2f}')
print(f'Tarifa variável total:                          |R$: {((tarifa_var_agua + tarifa_var_esgoto) * unidade):.2f}')

print('==*==' * 15)
print(f'Preço total por unidade de consumo:             |R$ {preco_unidade:.2f}')
print(f'Preço total total da fatura:                    |R$ {fatura:.2f}')
