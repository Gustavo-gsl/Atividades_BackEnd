def maximo(n1, n2):

    if n1 > n2:

        return n1
    
    elif n2 > n1:

        return n2

    else:

        return print("\nOs números são iguais")

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("\nInforme o segundo número: "))

print()
print(maximo(n1, n2))