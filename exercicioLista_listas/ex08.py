# 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
# ordem lida.

pessoas = []
for x in range (0, 5):
    pessoa = []
    pessoa.append(input('Informe idade: '))
    pessoa.append(input('Informe altura: '))
    pessoas.append(pessoa)

pessoas.reverse()
for pessoa in pessoas:
    print(f'Altura {pessoa[1]} / Idade: {pessoa[0]}')

