#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).


F = int(input("Informe a temperatura em F: "))
C = 5 * ((F-32) / 9)
print(F, "graus Fahrenheit, equivalem a", C, "graus Celsius.")