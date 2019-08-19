# Calculo do imposto de renda com base nas faixas de salário, para salarios acima de 3000 aliquota de 35%
# salarios entre 1000 e 3000 aliquota de 20% e salários de até 1000 estão isentos.

# Inicialização de váriaveis
salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario
imposto = 0
# Inicio das verificações
#Salários maiores que 3000
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
# Salários maiore que 1000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print("Salário: R$%.2f Imposto a pagar: R$%.2f" % (salario, imposto))
