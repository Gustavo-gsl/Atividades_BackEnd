# Atividade 4
## Questões
1. [Questão 4.8](#questão-48)

2. [Questão 4.9](#questão-49)

3. [Questão 4.10](#questão-410)
## Questão 4.8
```python
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
```
[| Arquivo da questão |](q4_8.py)
## Questão 4.9
```python
valorCasa = float(input("Informe o valor total da casa: "))
salario = float(input("Informe o seu salário: "))
valorPrestacao = valorCasa / (12 * float(input("Informe em quantos anos a casa será quitada: ")))

if(valorPrestacao > salario * 30/100):

    print("\n\nO valor da prestação é R$ "f"{valorPrestacao:.2f}"" que representa mais de 30% do seu salário.")
    print("Logo sua solicitação de empréstimo foi NEGADA.")

else:

    print("\n\nSua solicitação de empréstimo foi APROVADA.")
```
[| Arquivo da questão |](q4_9.py)
## Questão 4.10
```python
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
```
[| Arquivo da questão |](q4_10.py)