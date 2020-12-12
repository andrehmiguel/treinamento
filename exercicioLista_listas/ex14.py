# 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
# crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma
# classificação sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como
# "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
# contrário, ele será classificado como "Inocente".


quantidade_positivo = 0
status = {2: "Suspeito(a)",
          3: "Cúmplice",
          4: "Cúmplice",
          5: "Assassino"}

lista_perguntas = ["Telefonou para a vítima?",
                   "Esteve no local do crime?",
                   "Mora perto da vítima?",
                   "Devia para a vítima?",
                   "Já trabalhou com a vítima?"]

for i in range(len(lista_perguntas)):
    print(lista_perguntas[i] + " (sim ou não).")

    resposta = input("Resp.:")

    if resposta.lower() == "sim":
        quantidade_positivo += 1

if quantidade_positivo in status:
    print(status[quantidade_positivo])
else:
    print("Inocente")