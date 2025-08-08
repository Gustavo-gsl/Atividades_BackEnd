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