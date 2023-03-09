import numpy as np

#-------------MATRIZ RANDOM

#Numpy tiene un metodo para crear matrices aleatorias

matriz_random = np.random.randint(10, size=(5, 3))

print(matriz_random)
print('')

#no enteros menores que 1:

matriz_random2 = np.random.rand(3,3)

print(matriz_random2)
print('')



#---- EJERCICIO DE LOS DADOS QUE EL BOBO DE YT NO SABE COMO HACER

dadosPar = np.random.choice(a = [2,4,6], size=5)

print(dadosPar)
print('')


#Si le asignamos la probabilidad de que salga cada uno:

dadosParProb = np.random.choice(a = [2,4,6], p=[0.2, 0.1, 0.7] ,size=5)
print(dadosParProb)
print('')
