# Contagem regressiva para o lançamento de um foguete
import time # Importando a livraria time, temos acesso a várias funções ligadas ao tempo
x = 10
while x >= 0:
    print(x)
    time.sleep(2) # a função sleep da biblioteca time, faz com que códigos tenham um delay 
                  #entre um passo e outro, passamos um valor em segundos como parametro para    esse função.
    x = x - 1 # Contador fazendo a decrementação do valor inicial

print("Fogo!") # Contagem terminada é impresso em tela a palavra fogo.
