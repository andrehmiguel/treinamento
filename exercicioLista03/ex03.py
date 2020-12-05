# 03 Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Insira seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Informe seu salário: '))
sexo = input('Qual seu sexo (f / m): ')
estado_civil = input('Estado civil (s, c, v ou d): ')

while(len(nome) < 4):
    nome = input('Insira nome com mais de 3 caracteres: ')

while 0 > idade or 150 < idade:
    idade = int(input('Idade inválida! Digite uma idade entre 0 e 150 anos: '))

while salario <= 0:
    salario = float(input('Salário inválido! Informe seu salário: '))

while sexo != "F" and sexo != "f" and sexo != "M" and sexo != "m":
    sexo = input('Informação inválida. Qual seu sexo (f / m): ')

while (estado_civil != 's') and (estado_civil != 'c') and (estado_civil != 'v') and (estado_civil != 'd'):
    estado_civil = input('Insira um estado civil válido. As opções são (s, c, v ou d): ')

print('Todas as informações são válidas.')