#04 Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.


nome = input("Digite seu nome: ")
i = 0
while i < len(nome):
    print(nome[:i])
    i += 1

