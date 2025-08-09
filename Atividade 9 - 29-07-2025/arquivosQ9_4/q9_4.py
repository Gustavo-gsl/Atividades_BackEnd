def uneArq(arquivo1, arquivo2):

    arq1 = open(arquivo1, "r")
    arq2 = open(arquivo2, "r")
    arq3 = open("Atividade 9 - 29-07-2025/arquivosQ9_4/arquivoUniao.txt", "w")

    for linha1 in arq1.readlines():
    
        arq3.write(linha1)
    
    for linha2 in arq2.readlines():

        arq3.write(linha2)

    arq1.close()
    arq2.close()
    arq3.close()

arqEnter1 = input("\nInforme o nome do primeiro arquivo que deseja abrir\nLembre de usar o seguinte path -> Atividade 9 - 29-07-2025/arquivosQ9_4/\n\n")
arqEnter2 = input("\n\nInforme o nome do segundo arquivo que deseja abrir\nLembre de usar o seguinte path -> Atividade 9 - 29-07-2025/arquivosQ9_4/\n\n")

uneArq(arqEnter1, arqEnter2)

print("\n\nUnião bem sucedida!")