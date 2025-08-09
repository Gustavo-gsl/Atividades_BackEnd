def validar_nome_usuario(nome_entrada):
    
    nome_entrada = nome_entrada.strip().lower()

    return nome_entrada.isalnum(), nome_entrada

nome = input("Informe o nome que deseja colocar para normalizá-lo e validá-lo:\n")

if validar_nome_usuario(nome)[0] == True:
    
    print("\nNome: \"%s\" é válido " % validar_nome_usuario(nome)[1])

else:

    print("\nNome: \"%s\" não é válido" % validar_nome_usuario(nome)[1])