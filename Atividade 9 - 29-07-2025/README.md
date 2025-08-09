# Atividade 9 
## Questões
1. [Questão 9.3](#questão-93)

2. [Questão 9.4](#questão-94)

3. [Questão 9.5](#questão-95)

## Questão 9.3
```python
arquivoI = open("Atividade 9 - 29-07-2025/arquivosQ9_3/impares.txt", "r")
arquivoP = open("Atividade 9 - 29-07-2025/arquivosQ9_3/pares.txt", "r")
arquivoPI = open("Atividade 9 - 29-07-2025/arquivosQ9_3/pareseimpares.txt", "w")

valores = []
for linhaI in arquivoI.readlines():

    numero = int(linhaI)
    valores.append(numero)

for linhaP in arquivoP.readlines():

    numero = int(linhaP)
    valores.append(numero)

valores.sort()

for valor in valores:

    arquivoPI.write(f"{valor}\n")

arquivoI.close()
arquivoP.close()
arquivoPI.close()

print("\n\nUnião bem sucedida!")
```
[| Arquivo da questão |](/Atividade%209%20-%2029-07-2025/arquivosQ9_3/q9_3.py)
### Arquivos relacionados
[- impares.txt -](/Atividade%209%20-%2029-07-2025/arquivosQ9_3/impares.txt)

[- pares.txt -](/Atividade%209%20-%2029-07-2025/arquivosQ9_3/pares.txt)
## Questão 9.4
```python
def uneArq(arquivo1, arquivo2):

    arq1 = open(arquivo1, "r")
    arq2 = open(arquivo2, "r")
    arq3 = open("Atividade 9 - 29-07-2025/arquivosQ9_4/arquivoUniao.txt", "w")

    for linha1 in arq1.readlines():
    
        arq3.write(linha1)
    
    for linha2 in arq2.readlines():

        arq3.write(linha2)

    arq1.close()
    arq2.close()
    arq3.close()

arqEnter1 = input("\nInforme o nome do primeiro arquivo que deseja abrir\nLembre de usar o seguinte path -> Atividade 9 - 29-07-2025/arquivosQ9_4/\n\n")
arqEnter2 = input("\n\nInforme o nome do segundo arquivo que deseja abrir\nLembre de usar o seguinte path -> Atividade 9 - 29-07-2025/arquivosQ9_4/\n\n")

uneArq(arqEnter1, arqEnter2)

print("\n\nUnião bem sucedida!")
```
[| Arquivo da questão |](/Atividade%209%20-%2029-07-2025/arquivosQ9_4/q9_4.py)
### Arquivos relacionados
[- arquivo1.txt -](/Atividade%209%20-%2029-07-2025/arquivosQ9_4/arquivo1.txt)

[- arquivo2.txt -](/Atividade%209%20-%2029-07-2025/arquivosQ9_4/arquivo2.txt)

[- arquivo3.txt -](/Atividade%209%20-%2029-07-2025/arquivosQ9_4/arquivo3.txt)

[- arquivo4.txt -](/Atividade%209%20-%2029-07-2025/arquivosQ9_4/arquivo4.txt)
## Questão 9.5
```python
arqP = open("Atividade 9 - 29-07-2025/arquivosQ9_5/pares.txt", "r")

x = 0
for linha in arqP.readlines():

    x += 1

conteudo = [0] * x

arqP.close()

arqP = open("Atividade 9 - 29-07-2025/arquivosQ9_5/pares.txt", "r")

for linha in arqP.readlines():

    conteudo[x-1] = int(linha)
    x -= 1

arqP.close()

arqP = open("Atividade 9 - 29-07-2025/arquivosQ9_5/pares.txt", "w")

for numero in conteudo:

    arqP.write(f"{numero}\n")

arqP.close()

print("\n\nOperação completa!")
```
[| Arquivo da questão |](/Atividade%209%20-%2029-07-2025/arquivosQ9_5/q9_5.py)
### Arquivos relacionados
[- pares.txt -](/Atividade%209%20-%2029-07-2025/arquivosQ9_5/pares.txt)