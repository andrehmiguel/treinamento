#Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando
#outros símbolos em lugar das letras, como números por exemplo. A própria palavra
#leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma
#subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito
#usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise
#sobre as principais formas de traduzir as letras. Depois, faça um programa que peça
#uma texto e transforme-o para a grafia leet speak.

texto = input('Digite um texto para transformar em L337 $p34k: ')
dicionario = {
    'a': '4',
    'A': '4',
    'b': '8',
    'B': '8',
    'e': '3',
    'E': '3',
    'i': '1',
    'I': '1',
    'o': '0',
    'O': '0',
    's': '$',
    'S': '$',
    't': '7',
    'T': '7',}

for original, novo in dicionario.items():
    texto = texto.replace(original, novo)
print(f'mensagem traduzida: {texto}')