# Calcula o valor do aumento de um salário em função de um valor de aumento informado para o usuário

salario = float(input("Informe o valor do salário: "))
porcentagem = float(input("Informe a porcentagem do aumento: "))

aumento = salario * porcentagem / 100

#Ultilizando o padrao mais recente do format.
print(f"Sálario: R${salario:5.2f} \nAumento: R${aumento:5.2f} \nNovo salário: R${(salario + aumento):5.2f}")
