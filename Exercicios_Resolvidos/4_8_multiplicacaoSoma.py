a = int(input("Informe o primeiro numero: "))
b = int(input("Informe o segundo numero: "))

res = 0
x = 0

while x < b:
    res = res + a
    x = x + 1

print("%d x %d = %d" % (a, b, res))
