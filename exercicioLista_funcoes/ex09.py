# 9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro
# informado. Por exemplo: 127 -> 721.

def reverso(num):
    return str(num)[::-1]

num = str(input('Insira um número inteiro: ')).strip()
print(f'O número {num} revertido é -> {reverso(num)}')