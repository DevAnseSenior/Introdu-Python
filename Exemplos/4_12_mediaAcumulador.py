# Calculo de média aritmética
x = 1
soma = 0
while x <= 5:
    n = int(input("%d Digite o número: " % x))
    soma = soma + n
    x = x + 1
print("Média: %5.2f" % (soma/5))
