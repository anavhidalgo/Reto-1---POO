def anagramas(a):
    n = []
    m = len(a)
    for i in range(m):
        for j in range(i + 1, m): 
            if sorted(a[i]) == sorted(a[j]): #Ordena los caracteres de las palabras y compara
                n.append((a[i], a[j]))
    return n

p = ['amor', 'roma', 'perro']
y = anagramas(p)
print('Los elementos que tienen los mismos caracteres son:', y)