# Calcula o preço de uma viagem, através da distância dessa viagem

distancia = int(input("Informe a distância da viagem(Km): "))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print("Distancia da viagem: %dKm \nPreço do ticket: R$%.2f"
      %(distancia, passagem))
