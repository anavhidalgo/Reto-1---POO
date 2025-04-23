def primo(n):
  if n < 2:
    return False
  s = True
  m = int(n**0.5)
  for i in range(2, m+1):
    s = s and (n%i != 0)
  return s

def primos_en_arreglo(a):
  p = []
  for i in a:
    if primo(i):
      p.append(i)
  return p

q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = primos_en_arreglo(q)
print('Los primos en el arreglo son:', y)
