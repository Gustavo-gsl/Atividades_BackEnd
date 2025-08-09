def areaT(b, h):

    return (b * h)/2

b = float(input("Informe a base do triângulo: "))
h = float(input("Informe a altura do triângulo: "))

print()
print("{:.2f}".format(areaT(b, h)))