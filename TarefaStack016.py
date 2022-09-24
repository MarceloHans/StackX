# Algoritmo Tarefa 016: Três Valores e o Maior Deles (IF)
# Dev: Marcelo Hans Alexandre
# Data 15.09.2022
 
ValorA = int(input("Digite o 1º valor: "))
ValorB = int(input("Digite o 2º valor: "))
ValorC = int(input("Digite o 3º valor: "))

if ValorA > ValorB and ValorA > ValorC:
    print("O maior valor é: ", ValorA)
if ValorB > ValorA and ValorB > ValorC:
    print("O maior valor é: ", ValorB)
if ValorC > ValorA and ValorC > ValorB:
    print("O maior valor é: ", ValorC)