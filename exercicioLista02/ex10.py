#10. Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

def conversao(numero):
    conjunto_num = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
        80: 'oitenta', 90: 'noventa',}

    if numero < 20 or numero % 10 == 0:
        return conjunto_num.get(numero)

    decimal = numero // 10 * 10
    unidade = numero % 10
    extenso = f'{conjunto_num.get(decimal)} e {conjunto_num.get(unidade)}'
    return extenso


if __name__ == '__main__':
    numero = int(input('Insira um número: '))
    while numero > 99 or numero < 0:
        numero = int(input("Número inválido. Digite um número de 0 até 99: "))
    extenso = conversao(numero)
    print(f'Você digitou o número {extenso}.')
