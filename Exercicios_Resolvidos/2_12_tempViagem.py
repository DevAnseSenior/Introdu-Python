# Dado a distancia e velocidade media de uma viagem, Calcula-se o tempo de viagem em minutos.

distancia = float(input("Quantos km de viagem? "))
velocidade = int(input("Informe a velocidade média do veículo: "))

tempo = (distancia / velocidade)*60

print("O tempo previsto para a viagem é de: %d minuto(s)" % tempo)
