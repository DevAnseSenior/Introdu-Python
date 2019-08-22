# Programa que identifica uma categoria e mostra um preço atribuido a ela.

# Entrada de dados
categoria = int(input("Informe a categoria do produto: "))

# Busca pela categoria informada
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida.") # Retorno caso a categoria seja inválida
    preco = 0

# Exibição da saída
print("Valor do produto: R$%.2f" % preco)
    
