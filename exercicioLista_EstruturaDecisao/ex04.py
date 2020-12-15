# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante

letra = input('Insira uma letra para verificar: ')

vogal = 'aeiou'

if letra in vogal:
    print(f'A letra {letra.upper()} é vogal')
else:
    print(f'A letra {letra.upper()} é consoante')