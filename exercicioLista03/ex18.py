# 18. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5!=5.4.3.2.1=120

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


fatorial = int(input("Digite um número para saber o fatorial: "))
i = 0
lista=[]

while i < fatorial:
    i = i + 1
    lista.append(i)
    fatorial = fatorial * (fatorial - i)

print(lista)
print(fatorial)