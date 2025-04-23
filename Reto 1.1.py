a = int(input('Inserte el primer número: '))
b = int(input('Inserte el segundo número: '))
c = str(input('Inserte el operador: '))

def operaciones(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        return 'Operador no válido'

print('El resultado es: ', operaciones(a, b, c))