# Calcula a tarifa mensal de uma operadora de celular, seleciona o preço por minuto com base no consumo

# Entrada
minutos = int(input("Quantos minutos você utilizou este mês: "))

# Seleção da faixa de preços
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15

# Exibição do resultado
print("Você vai pagar este mês: R$%.2f" % (minutos * preco))
