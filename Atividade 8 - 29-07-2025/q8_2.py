def multiplo(n1, n2):

    if n1 % n2 == 0:

        return True
    
    else:

        return False

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("\nInforme o segundo número: "))

print()
print(multiplo(n1, n2))