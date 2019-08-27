# Resolução de uma divisão com sucessivas subtrações
dividendo = int(input("Informe o valor do dividendo: "))
divisor = int(input("Informe o valor do divisor: "))
resto = dividendo # Resto recebendo dividendo pra preservação de valor.
quociente = 0
# Enquanto o resto for maior ou igual ao divisor
while resto >= divisor:
    resto = resto - divisor # Subtração sendo executada
    quociente = quociente + 1 # Quociente soma mais um

# Exibição resultados. Entradas, quociente e resto
print("%d / %d = %d \nResto: %d" % (dividendo, divisor, quociente, resto))
