valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor
while True:
    if round(atual, 2) <= round(apagar, 2):
        apagar -= round(atual, 2)
        cedulas += 1
    else:
        if atual >= 1:
            print("%d cédula(s) de R$%d" % (cedulas, atual))
        else:
            print("%d moeda(s) de R$%.2f" % (cedulas, atual))
        if atual == 0:
            print("Contagem encerrada.")
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0
        cedulas = 0
