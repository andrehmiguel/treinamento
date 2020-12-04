"""O IMC (Índice de Massa Corporal) é um índice utilizado para detectar casos de obesidade ou desnutrição,
principalmente em estudos que envolvem grandes populações. Para a avaliação de um paciente individualmente,
no entanto, ele pode ser falho por não levar em conta a composição desse peso corporal, que pode ser composto por gordura, músculos, água e estruturas ósseas.

O IMC é calculado dividindo o peso pela altura elevada ao quadrado.

Tabela de resultados - IMC

O IMC pode trazer os seguintes resultados:

IMC 	Resultado
Menos do que 18,5 	Abaixo do peso
Entre 18,5 e 24,9 	Peso normal
Entre 25 e 29,9 	Sobrepeso
Entre 30 e 34,9 	Obesidade grau 1
Entre 35 e 39,9 	Obesidade grau 2
Mais do que 40 	Obesidade grau 3

Poste a url do projeto com a resposta"""


print("Informe seu peso e altura para calcular o IMC.")
peso = float(input("Peso (Kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC {imc:.01f} = Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'IMC {imc:.01f} = Você está com peso normal.')
elif imc >= 25 and imc <30:
    print(f'IMC {imc:.01f} = Você está com sobrepeso')
elif imc >= 30 and imc <35:
    print(f'IMC {imc:.01f} = Você está com obesidade grau 1')
elif imc >= 35 and imc <40:
    print(f'IMC {imc:.01f} = Você está com obesidade grau 2')
else:
    print(f'IMC {imc:.01f} = Você está com obesidade grau 3')


