salario = float(input("Informe o valor do salário: "))
porcentagemAumento = float(input("\nInforme o aumento (sem o símbolo %): "))

valorAumento = round(salario * porcentagemAumento / 100, 2)
novoSalario = salario + valorAumento

print("\nAumento: R$"f"{valorAumento:.2f}")
print("Novo salário: R$"f"{novoSalario:.2f}")