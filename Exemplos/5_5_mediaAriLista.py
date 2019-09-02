# Calcula a média aritmética com notas passadas em uma lista
nota = [6,7,5,8,9] # Atribuindo 5 notas a uma lista chamada nota.
soma = 0 
x = 0
while x < 5:
    soma += nota[x] # Somando o conteudo da lista nota[x](Na posição x) ao acumulador soma.
    print("Iteração %d -> Soma: %d" % (x, soma)) # Mostra o numero da iteração e o estado da váriavel soma durante
    x += 1
# Exibição do resultado
print("Média: %.2f" % (soma / x))
