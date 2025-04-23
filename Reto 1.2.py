a = str(input('Introduce una palabra: '))

def palindromo(a):
    s = len(a)
    for i in range(s // 2):
        if a[i] == a[s - i - 1]: #se recorre la palabra desde el principio y desde el final
            continue
        return False
    return True
            
if palindromo(a):
    print('La palabra ', a, 'es un palindromo')
else:
    print('La palabra ', a, 'no es un palindromo')
