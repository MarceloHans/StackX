# Algoritmo Tarefa 001: Gratificação de Natal
# # Dev: Marcelo Hans Alexandre
# Data 09.08.2022

HorasExtras = float(input("Digite o número de horas extras: "))
HorasFaltas = float(input("Digite o número de horas faltantes: "))

TotalMinutos = (HorasExtras - (2/3*HorasFaltas)) * 60

if TotalMinutos >= 2401:
    print("Minutos totais: ", TotalMinutos, "com gratificação de R$ 500,00")
elif TotalMinutos >= 1801 and TotalMinutos < 2401:
    print("Minutos totais: ", TotalMinutos, "com Gratificação de R$ 400,00")
elif TotalMinutos >= 1201 and TotalMinutos < 1801:
    print("Minutos totais: ", TotalMinutos, "com Gratificação de R$ 300,00")
elif TotalMinutos >= 601 and TotalMinutos < 1201:
    print("Minutos totais: ", TotalMinutos, "com Gratificação de R$ 200,00")
elif TotalMinutos < 601:
    print("Minutos totais: ", TotalMinutos, "com Gratificação de R$ 100,00")