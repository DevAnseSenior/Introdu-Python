# Aumento de salário através de faixas

#Entrada
salario = float(input("Informe o salário: "))

# Decisão por faixa
if salario > 1250:
    novoSalario = sal + (salario * 0.10)
if salario <= 1250:
    novoSalario = sal + (salario*0.15)

# Saída
print("Salário: R$%.2f \nNovo Salário: R$%.2f" %(salario, novoSalario))
