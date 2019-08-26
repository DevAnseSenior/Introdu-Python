# Tabuada de 1 a 10 de um numero dado pelo usuário

n = int(input("Tabuada de: "))
x = 1
while x <= 10:
    print("%d + %d = %d " % (n, x, n+x)) # Soma do numero digitado + contador
    x = x + 1                           # e exibição do resultado

