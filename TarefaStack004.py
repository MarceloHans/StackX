# Algoritmo Tarefa 004: Salário Bruto (IF)
# Dev: Marcelo Hans Alexandre
# Data 11.08.2022

SalarioBruto = float(input("Digite o seu salário bruto: "))
Imposto = 0.07*SalarioBruto

if SalarioBruto <= 350:
    SalarioLiquido = SalarioBruto - Imposto + 100
    print("O salário líquido é: ", SalarioLiquido)
elif SalarioBruto >= 351 and SalarioBruto <= 600:
    SalarioLiquido = SalarioBruto - Imposto + 75
    print("O salário líquido é: ", SalarioLiquido)
elif SalarioBruto >= 601 and SalarioBruto <= 900:
    SalarioLiquido = SalarioBruto - Imposto + 50
    print("O salário líquido é: ", SalarioLiquido)
else:
    SalarioLiquido = SalarioBruto - Imposto + 35
    print("O salário líquido é: ", SalarioLiquido)