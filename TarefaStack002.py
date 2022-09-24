# Algoritmo Tarefa 002: Idade e Peso (IF)
# # Dev: Marcelo Hans Alexandre
# Data 09.08.2022

Idade = int(input("Digite a sua idade: "))
Peso = float(input("Digite o seu peso: "))

if Idade < 20 and Peso <= 60:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 9!")
elif Idade < 20 and Peso > 60 and Peso <= 90:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 8!")
elif Idade < 20 and Peso > 90:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 7!")
elif Idade >= 20 and Idade < 50 and Peso <= 60:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 6!")
elif Idade >= 20 and Idade < 50 and Peso > 60 and Peso <= 90:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 5!")
elif Idade >= 20 and Idade < 50 and Peso > 90:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 4!")
elif Idade > 50 and Peso <= 60:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 3!")
elif Idade > 50 and Peso > 60 and Peso <= 90:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 2!")
elif Idade > 50 and Peso > 90:
    print("Com", Idade, "anos e peso de", Peso, "quilos, você está no grau de risco 1!")