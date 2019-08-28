# Programa que representa uma caixa registradora, dado o codigo do produto e quantidade, ele exibe o valor total das compras
total = 0
while True:
    codigo = int(input("Informe o código do produto: "))

    if codigo == 1:
        preco = 0.50
        quantidade = int(input("Quantidade do produto: "))
        sub_total = preco * quantidade
        print("Sub-total: R$ %.2f\n\n" % sub_total)
    elif codigo == 2:
        preco = 1
        quantidade = int(input("Quantidade do produto: "))
        sub_total = preco * quantidade
        print("Sub-total: R$ %.2f\n\n" % sub_total)
    elif codigo == 3:
        preco = 4
        quantidade = int(input("Quantidade do produto: "))
        sub_total = preco * quantidade
        print("Sub-total: R$ %.2f\n\n" % sub_total)
    elif codigo == 5:
        preco = 7
        quantidade = int(input("Quantidade do produto: "))
        sub_total = preco * quantidade
        print("Sub-total: R$ %.2f\n\n" % sub_total)
    elif codigo == 9:
        preco = 8
        quantidade = int(input("Quantidade do produto: "))
        sub_total = preco * quantidade
        print("Sub-total: R$ %.2f\n\n" % sub_total)
    elif codigo == 0:
        break
    else:
        print("Código inválidado.")

    total = total + sub_total


print("Total da compras: R$ %.2f" % total)
