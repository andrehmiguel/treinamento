# 13. Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
# mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = 0
acima_media = {}

for x in range(len(meses)):
    temperatura.append(float(input(f'Insira a temperatura média de {meses[x]}: ')))
media = sum(temperatura) / len(meses)

for x in range(len(meses)):
    if(temperatura[x] > media):
        acima_media.update({meses[x] : temperatura [x]})

print(f'Média da temmperatura anual: {media:.2f}')
print(f'Meses com temperatura acima da média: {acima_media}')