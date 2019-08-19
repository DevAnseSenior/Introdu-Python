# Verifica se um veiculo foi multado, veiculo só é multado se ultrapassar 80km/h, com base nisso a multa se dá por R$ 5,00 a cada KM acima de 80.

velocidade = int(input("Informe a velocidade do veiculo: "))
if velocidade <= 80:
    print("Velocidade permitida.")
if velocidade > 80:
    print("Você foi multado: ")
    multa = (velocidade - 80) * 5
    print("Multa: R$%.2f" % multa)
