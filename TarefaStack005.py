# Algoritmo Tarefa 005: Empresa com 10 Funcionários (WHILE)
# Dev: Marcelo Hans Alexandre
# Data 21.08.2022

Laco1 = 1
Laco2 = True
Laco3 = True

while Laco1 <= 10:
    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0

    Codigo = input("Digite o código do funcionário: ")
    HoraTrabalhada = float(input("Digite as horas trabalhadas: "))

    while Laco2:
        Categoria = input("Digite a categoria do cargo: O ou G: ")
        if Categoria == "O" or Categoria == "G":
            Laco2 = False
        else:
            print("As categorias possíveis são O e G, digite novamente: ")
            continue
        break

    while Laco3:
        Turno = input("Digite a letra do turno de trabalho: M, V ou N: ")
        if Turno == "M" or Turno == "V" or Turno == "N":
            Laco3 = False
        else:
            print("Os turnos possíveis são M, V e N, digite novamente: ")
            continue
        break

    if Categoria == "G" and Turno == "N":
        ValorHora = 0.18 * SalarioMinimo
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if Categoria == "G" and Turno == "M" or Turno == "V":
        ValorHora = 0.15 * SalarioMinimo
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if Categoria == "O" and Turno == "N":
        ValorHora = 0.13 * SalarioMinimo
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if Categoria == "O" and Turno == "M" or Turno == "V":
        ValorHora = 0.10 * SalarioMinimo
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    print ("O código do funcionário é: ", Codigo);
    print ("As horas trabalhadas são: ", HoraTrabalhada);
    print ("O valor da hora é: ", ValorHora);
    print ("O salario inicial é: ", SalarioInicial);
    print ("O valor do auxilio alimentação é: ", AuxilioAlimentacao);
    print ("O salário final é: ", SalarioFinal);

    Laco1 = Laco1 + 1
    Laco2 = True
    Laco3 = True