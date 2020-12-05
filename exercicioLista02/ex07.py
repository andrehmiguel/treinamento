#07 Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
#conte: quantos espaços em branco existem na frase e quantas vezes aparecem as vogais a, e, i, o, u."""

frase = input("Digite uma frase: ")
vogais = 0
brancos = 0

for letra in frase:
    if letra == " ":
        brancos += 1
    elif letra in "aeiou":
        vogais += 1
print(f'A frase tem {vogais} vogais e {brancos} espaços em branco.')
