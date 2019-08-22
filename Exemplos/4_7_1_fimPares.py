# Imprime os numeros pares de 0 até um numero informado pelo usuario
fim = int(input("Informe o ultima posição da contagem: "))
x = 0 # Inicializando a contagem por 0

while x <= fim:
    if x % 2 == 0: # Um numero é par se o resto da sua divisão por 2 for igual a 0
        print(x) # Impressão de um numero par
    x = x + 1 # Independente se um numero é par ou não a contagem não para
