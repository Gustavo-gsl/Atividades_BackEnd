import locale
locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")

itens_venda = [

("Produto A Longo Nome", 150.75),
("Item B", 25.00),
("C-123", 12345.80),
("Dígito Simples", 5.99)

]

print("{0:^17}{1:>18}".format("Item", "Preço"))
print("{0:-^37}".format("-"))

x = 0
while x < len(itens_venda):

    preco = locale.currency(itens_venda[x][1], symbol=False, grouping=True)
    print("{0[0]:<25}{1:>10}".format(itens_venda[x], preco))
    x += 1