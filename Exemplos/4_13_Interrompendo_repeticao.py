# Exemplo de interrupção de repetição
s = 0 # Acumulador iniciado com zero
# Repetição será executada de forma indefinida
while True:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    # Se o usuário digita zero a repetição é interrompida
    if v == 0:
        break
    s = s + v

# Exibição do total acumulado
print("Total acumulado: %d" % s)
