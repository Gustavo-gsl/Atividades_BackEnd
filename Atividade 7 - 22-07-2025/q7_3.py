frase = list(input("Digite uma frase longa: ").lower())
frase = "".join(frase)

pesquisa = input("Digite o trecho que deseja pesquisar: ").lower()

pos = 0
while pos >= 0:

    pos = frase.find(pesquisa, pos)
    if pos >= 0:

        print("\nO trecho \"%s\"" % pesquisa, "foi encontrada na posição:", pos)
        pos += 1

print("\nAparições de \"%s\":" % pesquisa, frase.count(pesquisa))