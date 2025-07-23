valorCasa = float(input("Informe o valor total da casa: "))
salario = float(input("Informe o seu salário: "))
valorPrestacao = valorCasa / (12 * float(input("Informe em quantos anos a casa será quitada: ")))

if(valorPrestacao > salario * 30/100):

    print("\n\nO valor da prestação é R$ "f"{valorPrestacao:.2f}"" que representa mais de 30% do seu salário.")
    print("Logo sua solicitação de empréstimo foi NEGADA.")

else:

    print("\n\nSua solicitação de empréstimo foi APROVADA.")