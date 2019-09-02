# Releitura do exercicio anterior dessa vez sem utilizar a repetição interna(Repertições aninhamadas)
# Dessa vez contadores iniciados juntos
tabuada = 1
numero = 1
while tabuada <= 10:
    print("%d x %d = %d" %(tabuada, numero, tabuada * numero))
    numero += 1
    if numero == 11: # Só passo pra próxima temporada quando o contador numero atinge a posição 11
        print("\n")
        numero = 1
        tabuada += 1
