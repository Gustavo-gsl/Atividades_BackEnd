arquivoI = open("Atividade 9 - 29-07-2025/arquivosQ9_3/impares.txt", "r")
arquivoP = open("Atividade 9 - 29-07-2025/arquivosQ9_3/pares.txt", "r")
arquivoPI = open("Atividade 9 - 29-07-2025/arquivosQ9_3/pareseimpares.txt", "w")

valores = []
for linhaI in arquivoI.readlines():

    numero = int(linhaI)
    valores.append(numero)

for linhaP in arquivoP.readlines():

    numero = int(linhaP)
    valores.append(numero)

valores.sort()

for valor in valores:

    arquivoPI.write(f"{valor}\n")

arquivoI.close()
arquivoP.close()
arquivoPI.close()

print("\n\nUnião bem sucedida!")