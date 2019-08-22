# Executa e exibe o resultado de uma das quatro operações, informados os dois valores e a operção a ser executada

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))

op = input("Informe a operação a ser realizada('+' - soma, '-' - Subtração, '*' - Multiplicação e '/' - Divisão): ")

if op == "+":
    r = a + b
elif op == "-":
    r = a - b
elif op == "*":
    r = a * b
elif op == "/":
    r = a / b
else:
    print("Operação inválida.")

print("Resultado: %.1f" % r)
