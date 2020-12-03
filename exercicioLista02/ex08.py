#08 Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são
#palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços
#foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

frase = input("Digite uma frase e descubra se é um Palíndromo: ").replace(' ','')
inverso = frase[::-1]
if frase == inverso:
    print(f'A frase {frase} é palíndromo')
else:
    print('Não é palíndromo')