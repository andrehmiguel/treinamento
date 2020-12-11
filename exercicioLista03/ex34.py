# 34. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
# programa que leia as um conjunto indeterminado de temperaturas, e informe ao final
# a menor e a maior temperaturas informadas, bem como a média das temperaturas.

n_temperaturas = int(input("Quantidade de temperaturas que irá digitar: "))
temperaturas = []
n_temperatura = 1
for i in range(n_temperaturas):
    print("Temperatura n° ", n_temperatura)
    temperatura = temperaturas.append(float(input("Digite a temperatura: ")))
    n_temperatura += 1

print("Maior temperatura = ", max(temperaturas))
print("Menor temperatura = ", min(temperaturas))
print("Média = ", round(sum(temperaturas) / len(temperaturas), 2))