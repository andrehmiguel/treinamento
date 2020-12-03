#01 Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string1 = input('Digite uma String: ')
string2 = input('Digite outra String: ')
tamanho_string1 = len(string1)
tamanho_string2 = len(string2)
print(f'{string1}: {tamanho_string1} caracteres')
print(f'{string2}: {tamanho_string2} caracteres')


if tamanho_string1 == tamanho_string2:
    print("As strings possuem tamanhos iguais")
else:
    print("As strings possuem tamanhos diferentes")
if string1 == string2:
    print("As strings são iguais")
else:
    print("As strings são diferentes")

