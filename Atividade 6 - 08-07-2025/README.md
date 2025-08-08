# Atividade 6
## Questões
1. [Questão 6.2](#questão-62)

2. [Questão 6.3](#questão-63)

3. [Questão 6.11](#questão-611)

4. [Questão 6.12](#questão-612)

5. [Questão 6.13](#questão-613)

6. [Questão 6.17](#questão-617)

7. [Questão 6.18](#questão-618)
## Questão 6.2
```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1[:] + l2[:]

print(l3)
```
[| Arquivo da questão |](q6_2.py)
## Questão 6.3
```python
l1 = [6, 4, 5, 7, 3]
l2 = [3, 2, 4, 1]
l3 = l2[:]

x = 0
while x < len(l1):

    repetido = False

    y = 0
    while y < len(l2):

        if l2[y] == l1[x]:

            repetido = True

        y += 1
    
    if repetido == False:
        l3.append(l1[x])
    
    x += 1

print(l3)
```
[| Arquivo da questão |](q6_3.py)
## Questão 6.11
Não é possível substituir o primeiro [while]() por um [for](), pois, no primeiro caso de repetição, é necessário repetir até o momento em que o usuário quiser, sem definir variáveis anteriores que poderiam guardar a quantidade de números que o usuário desejaria adicionar. Logo, devido à estrutura do [for](), não é possível fazer sem uma outra variável.
```python
L=[]

while True:
    n=int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)

for x in L:
    print(x)
```
[| Arquivo da questão |](q6_11.py)
## Questão 6.12
```python
L=[1,7,2,4]
mínimo=L[0]
for e in L:
    if e < mínimo:
        mínimo = e
print(mínimo)
```
[| Arquivo da questão |](q6_12.py)
## Questão 6.13
```python
T = [-10, -8, 0, 1, 2, 5, -2, -4]

menorT = 0
maiorT = 0
mediaT = 0

for x in T:

    if x == T[0]:

        menorT = x
        maiorT = x
        
    if x < menorT:

        menorT = x

    if x > maiorT:

        maiorT = x

    mediaT += x

mediaT /= len(T)

print("A menor temperatura foi:", menorT)
print("A maior temperatura foi:", maiorT)
print("A média das temperaturas foi:", mediaT)
```
[| Arquivo da questão |](q6_13.py)
## Questão 6.17
```python
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
```
[| Arquivo da questão |](q6_17.py)
## Questão 6.18
```python
dicionario = {}
frase = "O rato"

for letra in frase:

    qntdLetra = 0
    x = 0

    if letra == " ":
        
        continue
    
    if letra not in dicionario:

        while x < len(frase):

            if letra == frase[x]:

                qntdLetra += 1
            
            x += 1
        
        dicionario[letra] = qntdLetra


print(dicionario)
```
[| Arquivo da questão |](q6_18.py)