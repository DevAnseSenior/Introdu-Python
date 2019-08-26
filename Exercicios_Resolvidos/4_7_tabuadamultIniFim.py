# Tabuada de multiplicação (1 a 10) de um numero dado pelo usuário

n = int(input("Tabuada de: "))
inicio = int(input("Informe o inicio da tabuada: ")) # Inicio do contador
fim = int(input("Informe o fim da tabuada: ")) # Fim do contador
if inicio <= fim: # A operação só pode ser executada se o inicio for maior que fim
    x = inicio
    while x <= fim:
        print("%d x %d = %d " % (n, x, n*x)) # Multiplicação do numero digitado * contador
        x = x + 1                           # e exibição do resultado
else: # Caso contrário
    print("O inicio não pode ser maior do que o fim.")
