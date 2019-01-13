# Program koji računa Fibonaccijev niz
# Pronađite i ispravite sintaksne greške

N = int(input('Upiši broj članova niza: '))
if N == 0:
    print('0')
elif N == 1:
  print('0 1')
else:
    print('0 1', end=' ')
    a, b = 0, 1
    for i in range(0, N + 1):
        c = a + b
        a, b = b, c
        print(c, end = ' ')
