#18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

#arquivo = float(input('Insira o tamanho do arquivo em MB: '))
#velocidade = float(input('Insira a velocidade da sua internet em Mbps: '))


tamanho = float(input('Tamanho do arquivo em MB: '))
vel_megabit = float(input('Velocidade de Internet Mbps: '))
vel_megabyte = vel_megabit / 8
tempo = tamanho / vel_megabyte
minutos = tempo / 60


print(f'Para realizar o download deste arquivo, o tempo aproximado é de {minutos:.02f} minutos.')

