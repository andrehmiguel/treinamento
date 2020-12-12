# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
# foram lidas. Imprima as consoantes.

listaChar = []
consoantes = 0
print ('Informe 10 caracters')
for x in range(10):
    listaChar.append(input(f'Informe o {x + 1}º caracter: '))
    char = listaChar[x]
    if(char not in ('a','e','i','o','u')):
        consoantes += 1
print(f'Foram inseridas {consoantes} consoantes.')
print(listaChar)