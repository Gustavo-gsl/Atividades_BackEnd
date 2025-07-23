qtdKWh = float(input("Informe quantos kWh foram consumidos: "))
tipoInstalacao = str(input("\nInforme o tipo de instalação :\nR - Residencial\nC - Comercial\nI - Industrial\n\n"))

while(tipoInstalacao != "R" and tipoInstalacao != "r" and tipoInstalacao != "C" and tipoInstalacao != "c" and tipoInstalacao != "I" and tipoInstalacao != "i"):
    
    print("\n\nTipo residencial INVÁLIDO\n")
    tipoInstalacao = str(input("Informe corretamente o tipo de instalação -\nR - Residencial\nC - Comercial\nI - Industrial\n\n"))

if(tipoInstalacao == "R" or tipoInstalacao == "r"):

    if(qtdKWh <= 500):

        print("\nO valor total a pagar é: R$"f"{qtdKWh * 0.4:.2f}")

    else:

        print("\nO valor total a pagar é: R$"f"{qtdKWh * 0.65:.2f}")

if(tipoInstalacao == "C" or tipoInstalacao == "c"):

    if(qtdKWh <= 1000):

        print("\nO valor total a pagar é: R$"f"{qtdKWh * 0.55:.2f}")

    else:

        print("\nO valor total a pagar é: R$"f"{qtdKWh * 0.6:.2f}")

if(tipoInstalacao == "I" or tipoInstalacao == "i"):

    if(qtdKWh <= 5000):

        print("\nO valor total a pagar é: R$"f"{qtdKWh * 0.55:.2f}")

    else:

        print("\nO valor total a pagar é: R$"f"{qtdKWh * 0.6:.2f}")