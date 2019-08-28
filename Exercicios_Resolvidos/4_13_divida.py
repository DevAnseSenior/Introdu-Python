# Programa para pagamento de divida com juros mensal, mostra o progresso dos pagamentos mês a mês
# Entradas
divida = float(input("Informe o valor da dívida: R$ "))
taxa = float(input("Juros mensal: "))
pagamento = float(input("Qual o valor mensal de pagamento: R$ "))
mes = 1
# Verificação da viabilidade de pagamento
if divida * (taxa / 100) > pagamento:
    print("Sua dívida não será paga nunca.")
else:
    saldo = divida
    juros_pg = 0 # acumulador
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento       # Juros em cima de parcela
        juros_pg = juros_pg + juros
        print("Saldo da dívida do mês %d é de: R$ %.2f" % (mes, saldo))
        mes += 1
    # Exibição de saída
    print("Para pagar uma dívida de R$%.2f, a %.2f %% de juros," % (divida, taxa))
    print(" você precisara de %d meses, pagando um total de R$ %.2f de juros." % (mes, juros_pg))
    print(" No ultimo mês, você teria um saldo residual de R$ %.2f a pagar." % (saldo))
        
    
