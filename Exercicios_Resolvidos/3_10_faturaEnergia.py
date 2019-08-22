# Calculo da tarifa de energia basado no consumo de energia e em faixas determinadas de preço

# Entradas
consumo = float(input("Informe o consumo do imóvel: "))
categoria = input("Informe a categoria da instalação: ") # Lembrando que a função input já retorna uma string, sem necessidades de "conversões" para o tipo string

# Decisão por categoria de instalação
if categoria == "R" or categoria == "r":
    if consumo <= 500: # Decisão por consumo de energia
        preco = 0.40
    else:
        preco = 0.65
elif categoria == "C" or categoria == "c":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif categoria == "I" or categoria == "i":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Categoria inválida.")
    preco = 0

# Exibição de resultados
print("\n\nTipo de Instalação: %s \nConsumo: %.1fKWh \nValor a pagar: R$%.2f" # Uso de marcadores
      % (categoria, consumo, (consumo * preco))) # Definição do que chamamos em sala de "Ordem de aparição".
