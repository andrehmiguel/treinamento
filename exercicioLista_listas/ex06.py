# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
# vetor a média de cada aluno, imprima o número de alunos com média maior ou igual
# a 7.0.

lista_nota = []
nota_aluno = []
lista3 = []

for x in range(10):
    media = 0
    nota_aluno = []
    print (f'_Aluno {x + 1}_')
    for y in range(4):
        nota_aluno.append(float(input(f'Nota {y + 1}: ')))
        media += nota_aluno[y]
        #print(media)
    media = media/4
    print(media)
    lista_nota.append(media)

for x in lista_nota:
    if x >= 7:
        lista3.append(x)

print('-**-' * 15)
print(f'Notas totais: {lista_nota}')
print(f'Notas acima de >= 7: {lista3}')
print(f'{len(lista3)} alunos obtiveram nota maior ou igual a 7.')
