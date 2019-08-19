# Calcula o valor do aumento de um salário em função de um valor de aumento informado para o usuário

salario = float(input("Informe o valor do salário: "))
porcentagem = float(input("Informe a porcentagem do aumento: "))

aumento = salario * porcentagem / 100

print("Sálario: R$%5.2f \nAumento: R$%5.2f \nNovo salário: R$%5.2f"
      % (salario, aumento, (salario + aumento)))
