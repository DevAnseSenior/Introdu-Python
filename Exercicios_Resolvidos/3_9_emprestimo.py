# Programa que decide se um empréstimo é liberado ou não, dependendo de alguns fatores calculados como valor da parcela e uma base salarial

#Entradas
valor = float(input("Informe o valor do imovel: "))
salario = float(input("Informe o valor do salario: "))
anos = int(input("Informe a quantidade de anos em que pretende realizar o pagamento: "))

# Calculos de parcelas
parcela = valor / (anos * 12) # Conversão de anos em meses
base = salario * 0.30 # Base armazena 30% do sálario

# Condições de aprovação
if parcela <= base:
    print("\n\nEmpréstimo aprovado! \nValor da parcela: R$%.2f \nMeses a pagar: %d meses." # condição verdadeira
          % (parcela, (anos*12)))
else:
    print("\n\nEmpréstimo recusado! Valor da parcela muito alto.") # condição falsa
    
