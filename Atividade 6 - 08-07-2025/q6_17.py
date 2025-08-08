estoque={ "tomate": [ 1000, 2.30],
"alface": [ 500, 0.45],
"batata": [ 2001, 1.20],
"feijão": [ 100, 1.50] }

venda = []
total = 0

while True:
    
    produto = input("Produto: ").lower()

    if produto == 'fim':
        break

    while produto not in estoque:

        print("\n\n| Produto não encontrado |")
        produto = input("\nDigite novamente o Produto: ").lower()

        if produto == 'fim':
            break  
    
    quantidade = int(input("Quantidade vendida: "))

    while True:
        
        erro = False

        while quantidade > estoque[produto][0]:

            erro = True

            print("\n\n| Quantidade insuficiente no estoque |")
            quantidade = int(input("\nDigite novamente a Quantidade: "))

        while quantidade < 1:

            erro = True

            print("\n\n| Quantidade inválida |")
            quantidade = int(input("\nDigite novamente a Quantidade: "))

        if erro == False:

            break

    venda.append([produto, quantidade])

print("\nVendas:\n")
for operação in venda:

    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade

    print("%12s: %3d x %6.2f = %6.2f" %
    (produto, quantidade,preço,custo))

    estoque[produto][0] -= quantidade
    total+=custo

print(" Custo total: %21.2f\n" % total)

print("Estoque:\n")
for chave, dados in estoque.items():

    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])