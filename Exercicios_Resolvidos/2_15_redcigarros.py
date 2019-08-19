# Calcula a redução de tempo de vida de um fumante em dias, com base nos cigarros consumidos diarimente e os anos de tabagismo.

cig_dia = int(input("Informe a quantidade de cigarros ao dia: "))
anos_fum = int(input("Informe a quantidade anos fumando: "))

red_minutos = anos_fum * 365 * cig_dia * 10 # Total de minutos perdidos
red_dias = red_minutos / 1440 # Convertendo minutos em dias perdidos

print("Redução do tempo de vida: %d dias" % red_dias)
