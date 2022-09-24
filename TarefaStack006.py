# Algoritmo Tarefa 006: Receber nomes e salários (While)
# Dev: Marcelo Hans Alexandre
# Data 05.09.2022

RendaPoupanca = float(input("Digite o salário do Carlos: "))
RendaFixa = RendaPoupanca / 3
Meses = 0

while RendaFixa <= RendaPoupanca:
	Meses += 1
	RendaPoupanca = RendaPoupanca * 1.02
	RendaFixa = RendaFixa * 1.05

print("Foram necessários", Meses, "meses para Joao igualar ou ultrapassar o valor de Carlos")
print("Joao terá", "%.2f" % RendaFixa, "reais")
print("E Carlos terá", "%.2f" % RendaPoupanca, "reais")