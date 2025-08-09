arqP = open("Atividade 9 - 29-07-2025/arquivosQ9_5/pares.txt", "r")

x = 0
for linha in arqP.readlines():

    x += 1

conteudo = [0] * x

arqP.close()

arqP = open("Atividade 9 - 29-07-2025/arquivosQ9_5/pares.txt", "r")

for linha in arqP.readlines():

    conteudo[x-1] = int(linha)
    x -= 1

arqP.close()

arqP = open("Atividade 9 - 29-07-2025/arquivosQ9_5/pares.txt", "w")

for numero in conteudo:

    arqP.write(f"{numero}\n")

arqP.close()

print("\n\nOperação completa!")