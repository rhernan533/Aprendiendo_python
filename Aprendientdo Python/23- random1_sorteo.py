import random

#La función randint() devuelve un número entero incluido entre los valores indicados.

dado1= random.randint(1,6)
print(dado1)

print('\n')

regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']
           
for sorteo in range(5):
    regalo = regalos[random.randint(0, 9)]
    print('Sorteo', sorteo + 1, ':', regalo)