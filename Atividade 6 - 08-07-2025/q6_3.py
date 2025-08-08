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