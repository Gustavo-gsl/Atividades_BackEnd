# Atividade 7
## Questões
1. [Questão 7.1](#questão-71)

2. [Questão 7.2](#questão-72)

3. [Questão 7.3](#questão-73)

4. [Questão 7.4](#questão-74)

5. [Questão 7.5](#questão-75)

## Questão 7.1
```python
palavra = list(input("Informe uma palavra: "))
indice = int(input("\nInforme qual caractere deseja alterar (Ex: Oi -> 1 = O | 2 = i): ")) - 1

while indice > len(palavra) - 1 or indice < 0:

    print("\n\n| Valor inadequado |")
    indice = int(input("\nInforme qual caractere deseja alterar (Ex: Oi -> 1 = O | 2 = i): ")) - 1

caractere = input("\nInforme o novo caractere para a posição %d: " % (indice + 1))

palavra[indice] = caractere
palavra = "".join(palavra)
print("\n", palavra)
```
[| Arquivo da questão |](q7_1.py)
## Questão 7.2
```python
def validar_nome_usuario(nome_entrada):
    
    nome_entrada = nome_entrada.strip().lower()

    return nome_entrada.isalnum(), nome_entrada

nome = input("Informe o nome que deseja colocar para normalizá-lo e validá-lo:\n")

if validar_nome_usuario(nome)[0] == True:
    
    print("\nNome: \"%s\" é válido " % validar_nome_usuario(nome)[1])

else:

    print("\nNome: \"%s\" não é válido" % validar_nome_usuario(nome)[1])
```
[| Arquivo da questão |](q7_2.py)
## Questão 7.3
```python
frase = list(input("Digite uma frase longa: ").lower())
frase = "".join(frase)

pesquisa = input("Digite o trecho que deseja pesquisar: ").lower()

pos = 0
while pos >= 0:

    pos = frase.find(pesquisa, pos)
    if pos >= 0:

        print("\nO trecho \"%s\"" % pesquisa, "foi encontrada na posição:", pos)
        pos += 1

print("\nAparições de \"%s\":" % pesquisa, frase.count(pesquisa))
```
[| Arquivo da questão |](q7_3.py)
## Questão 7.4
```python
informacoes = input("Informe as seguintes informações nessa estrutura -> Sobrenome, Nome, Cidade:\n").split(",")

x = 0
for espaco in informacoes:

    informacoes[x] = espaco.strip()
    x += 1

informacoes = "{0[1]} {0[0]} (de {0[2]})".format(informacoes)

print(informacoes)
```
[| Arquivo da questão |](q7_4.py)
## Questão 7.5
```python
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
```
[| Arquivo da questão |](q7_5.py)