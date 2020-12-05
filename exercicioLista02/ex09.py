#09 Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou
#inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

cpf_original = input('Digite seu CPF no formato xxx.xxx.xxx-xx: ')
cpf_numeros = (cpf_original.replace('.','')).replace('-','')
#9 primeiros dígitos
n1 = int(cpf_numeros[0])
n2 = int(cpf_numeros[1])
n3 = int(cpf_numeros[2])
n4 = int(cpf_numeros[3])
n5 = int(cpf_numeros[4])
n6 = int(cpf_numeros[5])
n7 = int(cpf_numeros[6])
n8 = int(cpf_numeros[7])
n9 = int(cpf_numeros[8])

#Conferir a formatação do CPF
checker1 = None
if len(cpf_original) == 14 and '.' in cpf_original[3] and '.' in cpf_original[7] and '-' in cpf_original[11]:
    checker1 = True
else:
    print('CPF em formato inválido.')

##############################################
#validar dígito1
checker2 = None
digito1_calculo = (n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2)
resto_digito1 = digito1_calculo % 11
digito1_subtraido = 11 - resto_digito1

if digito1_subtraido > 9:
    digito1 = 0
else:
    digito1 = digito1_subtraido

digito1_string = str(digito1)
if digito1_string == cpf_numeros[9]:
    checker2 = True

#############################################
#validar dígito2
checker3 = None
digito2_calculo = (n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (digito1 * 2)
resto_digito2 = digito2_calculo % 11
digito2_subtraido = 11 - resto_digito2

if digito2_subtraido > 9:
    digito2 = 0
else:
    digito2 = digito2_subtraido

digito2_string = str(digito2)
if digito2_string == cpf_numeros[10]:
    checker3 = True

#############################################
#casos de exclusão
checker4 = None
if ((cpf_numeros == '00000000000') or (cpf_numeros == '11111111111') or (cpf_numeros == '22222222222') or (cpf_numeros == '33333333333')
or (cpf_numeros == '44444444444') or (cpf_numeros == '55555555555') or (cpf_numeros == '66666666666') or (cpf_numeros == '77777777777')
or (cpf_numeros == '88888888888') or (cpf_numeros == '99999999999')):
    checker4 = True


###########################################
#final check
if (checker1 == True) and (checker2 == True) and (checker3 == True) and (checker4 == None):
    print(f'O CPF {cpf_original} é um CPF válido')
else:
    print(f'O CPF {cpf_original} não é um CPF válido.')