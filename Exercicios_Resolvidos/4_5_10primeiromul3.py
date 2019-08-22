# Imprime os 10 primeiros multiplos de 3
quantidade = 1 # quantidade de numeros multiplos
x = 1 # Contador
while quantidade <= 10: # O loop termina apartir do momento que a quantidade de números é 10
    if x % 3 == 0: # apartir do momento que um numero múltiplo é encontrado ele imprime.
        print("%dº: %d" % (quantidade, x)) # é impresso o valor referente a quantidade de numeros multiplos e o próprio número multiplo
        quantidade = quantidade + 1 # Quantidade contando + 1

    x = x + 1 # Contagem acontecendo
