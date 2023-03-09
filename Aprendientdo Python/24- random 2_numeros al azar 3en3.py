import random

#La función randrange() devuelve enteros que van desde un valor inicial a otro final separados entre sí un 
# número de valores determinados

print('\nValores posibles: 3, 6, 9, 12, 15')
for i in range(25):
    print(random.randrange(3, 16, 3), end=' ')