# Algoritmo Tarefa 017: Triângulo (IF)
# Dev: Marcelo Hans Alexandre
# Data 15.09.2022
 
ValorA = int(input("Digite a medida do lado A do triângulo: "))
ValorB = int(input("Digite a medida do lado B do triângulo: "))
ValorC = int(input("Digite a medida do lado C do triângulo: "))

if ValorA == ValorB and ValorA == ValorC:
    print("O triângulo é Equilátero.")
elif ValorA != ValorB and ValorA != ValorC:
    print("O triângulo é Escaleno.")
else:
    print("O triângulo é Isóscele.")