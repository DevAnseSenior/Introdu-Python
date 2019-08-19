# Informado os km percorridos pelo veículo e os dias com ele, gera o valor do aluguel

km = int(input("Quantidade de km percorridos pelo veículo: "))
dias = int(input("Quantidade de dias com o veículo: "))

valor_km = km * 0.15
valor_dias = dias * 60

a_pagar = valor_km + valor_dias

print("Valor a pagar: R$%.2f" % a_pagar)
