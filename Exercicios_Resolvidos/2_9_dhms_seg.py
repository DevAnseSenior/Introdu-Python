# Usuário informa dias, horas, minutos e segundos e o valor é convertido para segundos e resultado é mostrado a seguir.

d = int(input("Informe a quantidade de dias: "))
h = int(input("Informe a quantidade de horas: "))
m = int(input("Informe a quantidade de minutos: "))
s = int(input("Informe a quantidade de segundos: "))

# Convertendo valores para segundos
m_s = m*60
h_s = h*3600
d_s = d*86400

segundos = d_s + h_s + m_s + s # Soma de todos os valores convertidos

print("%d dia(s), %d hora(s), %d minuto(s) e %d segundo(s), convertidos em segundos é igual a: %ds"
      % (d, h, m, s, segundos)) # Lembrando que aqui são definida as ordens de aparição dos marcadores.
