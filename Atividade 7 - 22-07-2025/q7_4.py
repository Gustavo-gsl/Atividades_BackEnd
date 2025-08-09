informacoes = input("Informe as seguintes informações nessa estrutura -> Sobrenome, Nome, Cidade:\n").split(",")

x = 0
for espaco in informacoes:

    informacoes[x] = espaco.strip()
    x += 1

informacoes = "{0[1]} {0[0]} (de {0[2]})".format(informacoes)

print(informacoes)