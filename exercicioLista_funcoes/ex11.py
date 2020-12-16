# 11. Data com mês por extenso . Construa uma função que receba uma data no formato
# DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA .
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

import datetime as date


def data_mes():
    data = input('Informe uma data no formato DD/MM/AAAA: ').strip()
    print(f'A data informada é: {date.datetime.strptime(data, "%d/%m/%Y").strftime("%d de %B de %Y.")}')


data_mes()