# 12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura
# desses alunos.

alunos = []
totalunos = 5

for x in range(30):
    aluno = []
    alunos.append(int(input(f'Informe a idade do aluno {x + 1}: ')))
    alunos.append((float(input(f'Informe a altura do aluno { x + 1}: '))))
    alunos.append(aluno)

soma_alt = 0.0
for aluno in alunos:
    soma_alt += aluno[1]


media_alt = soma_alt / float(totalunos)

tot_baixos = 0
for aluno in alunos:
    if aluno[0] > 13 and aluno[1] <= media_alt:
            tot_baixos += 1

print(f'Existem {tot_baixos} alunos abaixo da média de altura que é de {media_alt}')