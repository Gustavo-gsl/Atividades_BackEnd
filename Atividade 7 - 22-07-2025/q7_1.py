palavra = list(input("Informe uma palavra: "))
indice = int(input("\nInforme qual caractere deseja alterar (Ex: Oi -> 1 = O | 2 = i): ")) - 1

while indice > len(palavra) - 1 or indice < 0:

    print("\n\n| Valor inadequado |")
    indice = int(input("\nInforme qual caractere deseja alterar (Ex: Oi -> 1 = O | 2 = i): ")) - 1

caractere = input("\nInforme o novo caractere para a posição %d: " % (indice + 1))

palavra[indice] = caractere
palavra = "".join(palavra)
print("\n", palavra)