T = [-10, -8, 0, 1, 2, 5, -2, -4]

menorT = 0
maiorT = 0
mediaT = 0

for x in T:

    if x == T[0]:

        menorT = x
        maiorT = x

    if x < menorT:

        menorT = x

    if x > maiorT:

        maiorT = x

    mediaT += x

mediaT /= len(T)

print("A menor temperatura foi:", menorT)
print("A maior temperatura foi:", maiorT)
print("A média das temperaturas foi:", mediaT)