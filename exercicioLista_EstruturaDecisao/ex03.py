# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
# escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo = input(f'Sexo: F - Feminino, M - Masculino: ').lower()
if sexo == 'f':
    print('Sexo Feminino')
elif sexo == 'm':
    print('Sexo Masculino')
else:
    print('Sexo Inválido')