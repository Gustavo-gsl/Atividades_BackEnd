valorProduto = float(input("Informe o valor do produto: "))
porcentagemDesconto = float(input("\nInforme o desconto (sem o símbolo %): "))

valorDesconto = round(valorProduto * porcentagemDesconto / 100, 2)
valorAPagar = valorProduto - valorDesconto

print("\nDesconto: R$"f"{valorDesconto:.2f}")
print("Valor a pagar: R$"f"{valorAPagar:.2f}")