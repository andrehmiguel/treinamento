#09 Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou
#inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

cpf = input("Digite seu CPF no formato xxx.xxx.xxx-xx: ")


if len(cpf) == 14 and '.' in cpf[3] and '.' in cpf[7] and '-' in cpf[11]:
    print(f'{cpf} é um CPF válido.')
else:
    print(f'{cpf} é um CPF inválido.')

