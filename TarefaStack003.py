# Algoritmo Tarefa 003: Idade do Nadador (IF)
# # Dev: Marcelo Hans Alexandre
# Data 11.08.2022

Idade = int(input("Digite a sua idade: "))

if Idade < 5:
    print("Não tem uma categoria para essa idade!")
elif Idade >= 5 and Idade <= 7:
    print("A categoria é: Infantil.")
elif Idade >= 8 and Idade <= 10:
    print("A categoria é: Juvenil.")
elif Idade >= 11 and Idade <= 15:
    print("A categoria é: Adolescente.")
elif Idade >= 16 and Idade <= 30:
    print("A categoria é: Adulto.")
else:
    print("A categoria é: Sênior.")