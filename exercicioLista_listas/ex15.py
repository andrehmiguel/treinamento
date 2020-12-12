# 15. Faça um programa que leia um número indeterminado de valores, correspondentes
# a notas, encerrando a entrada de dados quando for informado um valor igual a -1
# (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do
# outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo
# do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

# 15. Faça um programa que leia um número indeterminado de valores, correspondentes
# a notas, encerrando a entrada de dados quando for informado um valor igual a -1
# (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do
# outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo
# do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

valor = 0
lista = []
while valor != -1:
    valor = int(input('insira um valor'))
    if valor != -1:
        lista.append(valor)

print(lista)

lista.reverse()
for x in lista:
    print(x)

media = sum(lista) / len(lista)
print(f'media {media}')




acima_media = 0
abaixo_de_sete= 0
for valor in lista:
    if valor > media:
        acima_media += 1
    elif valor < 7:
        abaixo_de_sete += 1


print(f'acima da média: {acima_media}')
print(f'abaixo de 7: {abaixo_de_sete}')

