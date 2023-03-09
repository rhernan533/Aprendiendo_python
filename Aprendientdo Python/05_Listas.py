#Una lista es una forma de agrupar informacion en un solo lugar.

#ej de list:
meses = ["enero", "febrero", "marzo", "ablir", "mayo"]

#podemos ahora por ejermplo imprimir la lista meses de manera sencialla

print(meses) #no usamos comillas en meses porque no es un str

#si queremos acceder a un determinado valor de nuestra lista, tenemos que escribir el nombre de la lista y 
#entre corchetes la posicion del valor (se empiza a contar desde el cero)
#ej de acceder a enero, marzo y mayo e imprimirlos

print(meses[0], meses[2], meses[4])



#usaremos un metodo ahora para ordenar una lista. Un metodo es similar a una funcion podemos decir

nombres=["Hernán", "Juan", "Agustina", "Sofia", "Zara", "Segundo"]
print(nombres)
#El metodo para ordenar una lista es:
nombres.sort()
#Una vez ordenado los nombres por el metodo anterior, lo imprimimos
print(nombres)

#podemos remplazar uno de los valores
nombres[2] = "Valeria" 
print (nombres)

#agregar elementos
meses.append("junio")
print(meses)

#eliminar elemento
del nombres[0]
print(nombres)

#Otras formas de eliminar elementos:
nombres.pop()  #elimina el ultimo
print(nombres)
nombres.pop(2) #elimina el que le indicamos 
print(nombres)

nombres.remove("Sofia") #eliminar por nombre
print(nombres)