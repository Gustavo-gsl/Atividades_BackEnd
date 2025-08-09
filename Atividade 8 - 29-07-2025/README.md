# Atividade 8 
## Questões
1. [Questão 8.1](#questão-81)

2. [Questão 8.2](#questão-82)

3. [Questão 8.3](#questão-83)

4. [Questão 8.4](#questão-84)

## Questão 8.1
```python
def maximo(n1, n2):

    if n1 > n2:

        return n1
    
    elif n2 > n1:

        return n2

    else:

        return print("\nOs números são iguais")
    
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("\nInforme o segundo número: "))

print()
print(maximo(n1, n2))
```
[| Arquivo da questão |](q8_1.py)
## Questão 8.2
```python
def multiplo(n1, n2):

    if n1 % n2 == 0:

        return True
    
    else:

        return False

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("\nInforme o segundo número: "))

print()
print(multiplo(n1, n2))
```
[| Arquivo da questão |](q8_2.py)
## Questão 8.3
```python
def areaQ(l):

    return (l * l)

l = float(input("Informe o lado do quadrado: "))

print()
print("{:.2f}".format(areaQ(l)))
```
[| Arquivo da questão |](q8_3.py)
## Questão 8.4
```python
def areaT(b, h):

    return (b * h)/2

b = float(input("Informe a base do triângulo: "))
h = float(input("Informe a altura do triângulo: "))

print()
print("{:.2f}".format(areaT(b, h)))
```
[| Arquivo da questão |](q8_4.py)