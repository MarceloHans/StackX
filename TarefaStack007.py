# Algoritmo Tarefa 007: Conjunto de Valores (While)
# Dev: Marcelo Hans Alexandre
# Data 07.09.2022
 
import math

Valor = int(input("Para seguir digite um valor positivo. Para finalizar digite zero ou um valor negativo: "))

while Valor > 0:
    print("O valor informado foi:", Valor)
    print("O seu quadrado é:", (Valor**2))
    print("O seu cubo é:", Valor**3)
    print(f"A sua raiz quadrada é: {math.sqrt(Valor):,.2f}")
    Valor = int(input("Para seguir digite um valor positivo. Para finalizar digite zero ou um valor negativo: "))
    continue
print("Obrigado por usar nosso aplicativo!")