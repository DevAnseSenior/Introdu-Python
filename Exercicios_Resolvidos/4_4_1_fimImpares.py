# Imprime os números impares em um intervalo de 1 e um valor informado pelo usuário
fim = int(input("Informe o ultima posição da contagem: "))
x = 1

while x <= fim:
    if x % 2 != 0: # Se enquanto para numeros pares, o resto da divisão em python é dado pelo resto igual a zero, os impares se não pelos diferentes.
        print(x)
    x = x + 1
