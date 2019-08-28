# Exemplo de interrupção de repetição
soma = 0 # Acumulador iniciado com zero
contador = 0
# Repetição será executada de forma indefinida
while True:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    # Se o usuário digita zero a repetição é interrompida
    if v == 0:
        break
    soma += v
    contador = contador + 1


media = soma / contador
# Exibição do total acumulado
print("Soma: %d \nQuantidade: %d \nMédia: %d" % (soma, contador, media))
