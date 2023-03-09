nombres=["Hernán", "Juan", "Agustina", "Sofia", "Zara", "Segundo"]
#si quisieramos imprimir uno por uno los nombre, (no imprimir la lista sino los elementos de ella), lo 
#lo tendriamos que hacer de la siguiente manera:
print(nombres[0])
print(nombres[1])
print(nombres[2])
#etc...

#Pero esto se puede hacer usando solo una linea mediante un iterador:

for nombre in nombres:
 print (nombre)
#Nombre es como llamamos a cada elemento de nombres.
#entonces decimos, para cada elemnto de nombres hacer tal cosa. imprimir en nuestro caso 


#Otras formas de usar for:

for numeros in range (0,11):   #range podermos ver que es una funcion en la que podemos asignar un rango de numeros
    print (numeros)

#podemos agregar un valor mas a la funcion range que indica en cuanto crece. ej:

for numeros2 in range (0,11,2):   #range podermos ver que es una funcion en la que podemos asignar un rango de numeros
    print (numeros2)

for numeros3 in range (10,0,-2):  #para crear una cuenta decendente
    print (numeros3)