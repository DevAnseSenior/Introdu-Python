#Exercício que mostra as tabuadas de multiplicação de 1 a 10.
tabuada = 1 # Tabuada é o contador da primeira repetição, ele só é executado após o termina da repetição interna
while tabuada <= 10:
    print("\n") # Pulando uma linha
    numero = 1 #Numero contador da repetição interna
    while numero <= 10:
        print("%d x %d = %d" % (tabuada, numero, tabuada * numero)) # Impressão da tabuada de determinado numero, ate que este seja igual a 10
        numero += 1
    tabuada += 1
