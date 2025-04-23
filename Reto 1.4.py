def suma_consecutivos(a):
    n = []
    m = len(a)

    if m < 2:
        raise ValueError("La lista debe contener al menos dos elementos.")
    
    for i in range(m -1):
        sumas = a[i] + a[i + 1]
        n.append(sumas)
    return n

def mayor(n):

    mayor = n[0]
    for i in n:
        if i > mayor:
            mayor = i
    return mayor

p = [1, 2, 3, 4, 5]
y = suma_consecutivos(p)
z = mayor(y)
print('La mayor suma de consecutivos es:', z)