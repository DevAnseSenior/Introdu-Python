# Calculo de juros composto em cima de uma quantia inicial depositada pelo usuário

deposito_i = float(input("Informe o valor do depósito: ")) # Deposito inicial
investimento = float(input("Informe o depósito mensal: ")) # Depósito mensal
taxa_j = float(input("Informe qual a taxa de juros: ")) # Juros mensal

ganho_j = 0 # Variavel que vai armazenar o meu ganho total com juros
ganho_m = deposito_i # Ganhos mensais recebendo o deposito inicial, para que o valor dessa, seja preservado
mes = 1 # Contador que comanda o fluxo da repetição

while mes <= 24: #Enquanto o mês for menor ou igual a 24, a repetição vai acontecer
    juros = (ganho_m * taxa_j)/100 # Calcula o juros do mês em questão
    ganho_m = ganho_m + juros + investimento # Calculo dos ganhos
    print("Ganho do mês %d: R$ %.2f" % (mes, ganho_m)) # Exibe os ganhos do mês em questão
    ganho_j += juros # Acumulando o juros para o fim do periodo, o mesmo que ganho_j = ganho_j + juros
    mes += 1 # Passo dado no contador

# Exibição do resultado
print("\n\nDepósito inicial: R$ %.2f \nGanhos com Juros: R$ %.2f" % (deposito_i, ganho_j))
