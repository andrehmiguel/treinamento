# 8. Faça uma função que informe a quantidade de dígitos de um determinado número
# inteiro informado.


def digitos(num):
    return len(str(num))

num = str(input('Insira um número: ')).strip()
print(f'O número {num} possui {digitos(num)} dígitos.')
