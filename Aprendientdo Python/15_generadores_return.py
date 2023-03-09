#Cuando definimos una función tenemos las siguientes maneras de obtener el valor de la funcion: mediante
# "return"  o mediante "yield"
# Cuando usamos "return", el programa automaticamente reserva un espacio de memoria y automaticamente guarda
# el valor o todos los valores de la funcion.

#Imprimir pares con return:

pares = []  #Una lista donde se van a guardar los valores

def num_pares(limite):
    i=1
    while i<= limite:
        pares.append(i*2)  #append para añadir a la lista
        i+=1  
    return pares

print(num_pares(10))  # <--Cambiar el numero para cambiar la cantidad de n° que devuelve el programa  

# Vemos que el "return" reserva espacio en memoria y guarda todos los valores "de una" en la lista


