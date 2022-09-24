# Algoritmo Tarefa 015: Complemento ao Polígono da Tarefa 14 (IF)
# Dev: Marcelo Hans Alexandre
# Data 13.09.2022
 
import math

Lado = int(input("Digite o número de lados do polígono (3, 4 ou 5): "))
Verdade = 1

if Lado < 3:
    print("NÃO É UM POLÍGONO")
    Verdade = 0
if Lado > 5:
    print("POLÍGONO NÃO IDENTIFICADO")
    Verdade = 0

if Verdade == 1:
    Medida = int(input("Digite a medida de um lado do polígono (cm): "))

if Lado == 3:
    Area = (Medida ** 2 * math.sqrt(3)) / 4
    print(f"O seu polígono é um TRIÂNGULO e possui uma área de: {Area:,.2f} cm²")

if Lado == 4:
    Area = Medida ** 2
    print(f"O seu polígono é um QUADRADO e possui uma área de: {Area:,.2f} cm²")

if Lado == 5:
    Area = (5 * Medida ** 2) / (4 * math.sqrt(5 - 2 * math.sqrt(5)))
    print(f"O seu polígono é um PENTÁGONO e possui uma área de: {Area:,.2f} cm²")
