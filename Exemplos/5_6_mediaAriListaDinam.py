# Calculo da média aritmética através de lista, usuário informando o valor das notas
notas = [0,0,0,0,0] # Iniciando a listas com valores 0
soma = 0
x = 0
# Adicionando notas
while x < 5:
    notas[x] = float(input("Nota %d: " % x)) # Atribuindo o valor de forma dinâmica a nota[x](Na posição x)
    soma += notas[x]
    x += 1

x = 0 # Reiniciando o contador
# Mostrando notas
print("\n\nNotas do Bimestre: ")
while x < 5:
    print("Nota %d: %.2f" % (x, notas[x])) # Mostrando qual nota e o valor dela para o usuário(Estado atual da lista)
    x += 1
print("Média: %.2f" % (soma/x))
