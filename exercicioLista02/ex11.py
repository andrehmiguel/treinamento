#11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de
#palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador
#poderá errar 6 vezes antes de ser enforcado.
"""
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!
Digite uma letra: O
A palavra é: _ _ _ _ O
Digite uma letra: E
A palavra é: _ E _ _ O
Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""

from random import choice

def jogo_forca(forca):
    print(' '.join(forca).upper())
    print('')


conjunto = ['computador', 'casa', 'livro', 'abelha', 'arvore', 'python', 'caderno', 'relogio', 'mochila']
palavra = choice(conjunto)
forca = ['_' for i in range(len(palavra))]
erros = 0
ganhou = False

while erros < 6 and not ganhou:
    jogo_forca(forca)
    print('Digite uma letra:')
    chute = str(input()).lower()

    if chute not in palavra:
        erros += 1
        print(f'Você errou pela {erros}ª vez. Tente de novo!')
        continue

    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index] = chute

    if '_' not in forca:
        ganhou = True

if ganhou:
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu!')
jogo_forca(forca)