# Exercicio que converte valores informados em metros para milimetros

m = float(input("Digite o valor em metros: ")) # Variavel que representa os metros, do tipo ponto flutuante

mm = m * 1000 # Conversão sendo executada e armazenando o valor do calculo na váriavel mm

print("%.1fm = %.1fmm" % (m,mm)) # Exibição de resultados
