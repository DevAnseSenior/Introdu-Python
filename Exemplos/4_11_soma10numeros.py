# Calculo da soma de 10 numeros
n = 1 # Contador
soma = 0 # Acumulador
while n <= 10:
    x = int(input("Digite o %d número: " %n))
    soma = soma + x
    n += 1 # ==    n = n + 1
print("Soma: %d" % soma)
