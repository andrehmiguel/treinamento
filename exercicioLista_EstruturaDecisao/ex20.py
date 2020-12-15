# 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve
# calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva
# média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva
# média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

listanotas = []

try:
    for x in range(1,4):
        listanotas.append(float(input(f'Informe a nota {x}: ')))
except ValueError:
    print('Informe valor numérico.')

media = sum(listanotas) / len(listanotas)

if media >= 7 and media < 10:
    print(f'Sua média foi de {media} e você foi aprovado.')
elif media < 7:
    print(f'Sua média foi de {media} e você foi reprovado.')
else:
    print(f'Parabéns! Sua média foi de {media} e você foi aprovado com distinção!')