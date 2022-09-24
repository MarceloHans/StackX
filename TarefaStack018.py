# Algoritmo Tarefa 018: Ângulos do Triângulo (IF)
# Dev: Marcelo Hans Alexandre
# Data 15.09.2022
 
ValorA = int(input("Digite o 1º ângulo do triângulo (°): "))
ValorB = int(input("Digite o 2º ângulo do triângulo (°): "))
ValorC = int(input("Digite o 3º ângulo do triângulo (°): "))

if ValorA == 90 or ValorB == 90 or ValorC == 90:
    print("É um triângulo Retângulo.")
elif ValorA >= 90 or ValorB >= 90 or ValorC >= 90:
    print("É um triângulo Obtusângulo.")
else:
    print("É um triângulo Acutângulo.")