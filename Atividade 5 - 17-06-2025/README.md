# Atividade 5
## Questões
1. [Questão 5.1](#questão-51)

2. [Questão 5.4](#questão-54)

3. [Questão 5.5](#questão-55)

4. [Questão 5.6](#questão-56)

5. [Questão 5.8](#questão-58)
## Questão 5.1
```python
x = 1

while x <= 100:

    print(x)
    x += 1
```
[| Arquivo da questão |](q5_1.py)
## Questão 5.4
```python
fim = int(input("Digite o valor máximo do intervalo:"))
x = 1

while x <= fim:

    if (x % 2 != 0):

        print(x)
        x += 2
```
[| Arquivo da questão |](q5_4.py)
## Questão 5.5
```python
x = 1

while x <= 10:

    print(x * 3)
    x += 1
```
[| Arquivo da questão |](q5_5.py)
## Questão 5.6
```python
x = 1

while x <= 10:

    print("3 x", x,"=", x * 3)
    x += 1
```
[| Arquivo da questão |](q5_6.py)
## Questão 5.8
```python
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

x = 1
resultado = 0

while x <= n2:

    resultado += n1
    x += 1

print("\n\nO resultado da multiplicação é:", resultado)
```
[| Arquivo da questão |](q5_8.py)