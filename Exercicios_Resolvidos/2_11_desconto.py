# Calcula o percentual de desconto em um produto com base em uma porcentagem estipulada pelo estabelecimento

preco =  float(input("Informe o preço da mercadoria: "))
percentual = float(input("Informe o percentual do desconto: "))

desconto = preco * percentual / 100
a_pagar = preco - desconto

print("\n\nPreço: R$%.2f \nDesconto: R$%.2f \nPreço a pagar: R$%.2f" % (preco, desconto, a_pagar))
