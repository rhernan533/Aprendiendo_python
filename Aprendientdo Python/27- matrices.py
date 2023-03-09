import numpy as np


#--------------------------------CREAR MATRICES


matriz2x3 = np.array([[2,5,8], [1,8,9]])

matriz3x2= matriz2x3.reshape(3,2)  #reshape solo invirtiendo filas y columnas. No se puede reshape(1,0) x ej.


print(matriz2x3)
print('')
print(matriz3x2)
print('')

tamanio_matriz = matriz2x3.shape

print('las dimensiones de la matriz son (filas, columnas): {}'.format(tamanio_matriz))
print('')

#--------------------------------------------------------- MATRIZ NULA

matriz_nula_3 = np.zeros(3)
print(matriz_nula_3)
print('')

matriz_nula_4x4 = np.zeros((4, 4))
print(matriz_nula_4x4)
print('')

#--------------------------------------------------------- MATRIZ RANGO

matriz_rango = np.array(range(10))
print(matriz_rango)
print('')


#mas facil:
matriz_rango2= np.arange(10)
print(matriz_rango2)
print('')


#-----LINSPACE: crear matriz de elementos separados por una cantidad establecida.

matriz_patron = np.linspace(10, 70, 5) #crea una matriz con valores separados por una misma cantidad 
#en el rango solicitado.→matriz del 10 al 70 formada por 5 elementos

print(matriz_patron)
print('Numero de elementos: ' + str(matriz_patron.size))  #Dice el numero de elementos


#Otra nueva forma de concatar en un print con un str con otro tipo de dato es el siguiente:

print('Numero de elementos: {}'.format(matriz_patron.size))
print('')

#ej 2

matriz_patron2 = np.linspace(100, 0, 5)

print(matriz_patron2)
print('')



#-------------------------------MATRIZ 3D

matriz3D = np.arange(27).reshape(3,3,3) 
#reshape → 3 matrices de  3 filas y 3 columnas

print(matriz3D)
print('')
