# Algoritmo que faz a correção de uma avaliação baseado em um dado gabarito
# a -> b, b -> a e c -> d
pontos = 0 
questao = 1
# Enquanto questao não ultrapassa o valor 3
while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao) # Informa a resposta ao inicio de cada laço
    if questao == 1 and resposta == "b": # Verificação por questão e reposta dada
        pontos = pontos + 1
    if questao == 2 and resposta == "a":
        pontos = pontos + 1
    if questao == 3 and resposta == "d":
        pontos = pontos + 1
    questao += 1  # == questao = questao + 1
print("O aluno fez %d ponto(s)." % pontos) # Exibição de resultado
