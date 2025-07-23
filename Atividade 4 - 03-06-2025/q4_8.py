n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = int(input("Informe o número que representa a operação que deseja ( 1: + | 2: - | 3: * | 4: / ): "))

while(operacao < 1 or operacao > 4):

    print("| Escolha Inválida |\n\n")
    operacao = int(input("Escolha entre -\n1: +\n2: -\n3: *\n4: /\n\n"))

if(operacao == 1):

    print("\n\nA soma dos valores é:", n1+n2)

if(operacao == 2):

    print("\n\nA subtração dos valores é:", n1-n2)

if(operacao == 3):

    print("\n\nA multiplicação dos valores é:", n1*n2)

if(operacao == 4):
    
    print("\n\nA divisão dos valores é:", n1/n2)