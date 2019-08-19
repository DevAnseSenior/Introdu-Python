# Verifica qual o valor maior e menor entre três numeros.

n1 = int(input("Informe o valor do primeiro número: "))
n2 = int(input("Informe o valor do segundo número: "))
n3 = int(input("Informe o valor do terceiro número: "))

# Maior
if n1 > n2 and n1 > n3:
    print("Maior: %d" % n1)
if n2 > n1 and n2 > n3:
    print("Maior: %d" % n2)
if n3 > n1 and n3 > n2:
    print("Maior: %d" % n3)

# Menor
if n1 < n2 and n1 < n3:
    print("Menor: %d" % n1)
if n2 < n1 and n2 < n3:
    print("Menor: %d" % n2)
if n3 < n1 and n3 < n2:
    print("Menor: %d" % n3)

# Igualdade
if n1 == n2 and n2 == n3:
    print("Números iguais.")
