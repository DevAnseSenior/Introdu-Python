# Verifica a idade do carro com base na idade, carro novo se tiver até 3 anos, passando disso informa que o veículo é velho

idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")
