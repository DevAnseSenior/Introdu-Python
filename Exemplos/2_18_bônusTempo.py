# Calculo de bônus por anos de serviço

# Entrada de dados
anos = int(input("Anos de serviço: ")) # Entrada do tipo inteiro
valor_por_ano = float(input("Valor por ano: ")) # Entrada do tipo ponto flutuante

# Calculo do bônus com  as entradas colhidas
bônus = anos * valor_por_ano

# Exibição de resultado utilizando composição
print("Bônus de R$%5.2f" % bônus)   # %5.2f - Marcador de posição para numeros de ponto flutuante, no caso temos 5 posições em                                     
                                    # reserva, sendo que duas dessas posições são para casas decimais
