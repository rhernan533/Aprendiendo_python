import random

#La función random() devuelve un número float entre 0 y 1
print('Ejemplo 1:')
for numero in range(3):
    print(random.random(), end=' ')

print('\n')

#La función uniform() devuelve un número float incluido entre los valores indicados
print('Ejemplo 2:')
for numero in range(3):
    print(random.uniform(100, 105), end=' ')

print('\n')

#La función choice() se utiliza para seleccionar elementos al azar de una lista.
print('Ejemplo 3:')
transporte = ['bici', 'moto', 'coche', 'tren', 'avión']
print('Hoy viajaré en:', random.choice(transporte))

print('\n')

#La función shuffle() 'mezcla' o cambia aleatoriamente el orden de los elementos de una lista
print('Ejemplo 4:')
lista = ['rojo', 'verde', 'amarillo']

random.shuffle(lista)
print('mezcla1', lista)

random.shuffle(lista)
print('mezcla2', lista)
print(lista[random.randint(0,2)])

print('\n')

#La función sample() devuelve de una lista de elementos un determinado número de elementos diferentes elegidos 
# al azar.

print('Ejemplo 5:')

lista = ['x', 'y', 'z']
print(random.sample(lista, 2)) #devuelve dos elementos de una lista que contiene tres.


