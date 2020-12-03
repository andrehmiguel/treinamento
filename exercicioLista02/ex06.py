#06 Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.


from datetime import date, datetime

data = input(("Qual sua data de nascimento (dd/mm/aaaa): "))
print(f'Sua data de nascimento é {datetime.strptime(data, "%d/%m/%Y").strftime("%d de %B de %Y.")}')