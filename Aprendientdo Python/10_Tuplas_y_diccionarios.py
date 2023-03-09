# Tanto las listas como las tuplas y los diccionarios son variables que nos permiten agrupar varios datos

# a una TUPLA se la designa entre parentesis () 
# Una Tuplas es una variable que permite almacenar varios datos que no pueden ser modificados una vez creados

ej_tupla = ("texto", 15, 2.5,"hola", 8)

print(ej_tupla)

print (ej_tupla[1])
print(ej_tupla [0:2])
print (ej_tupla [:3])
print (ej_tupla [2:])

print("")
# a un DICCIONARIO se lo asigna por llaves {}
# Mientras que a las listas y tuplas se accede solo y únicamente por un número de índice,los diccionarios 
# permiten utilizar una clave para declarar y acceder a un valor


hernan = {
    "nombre" : "Gustavo Hernán",
    "apellido" : "Herrera Rodriguez",
    "edad" : 19,
    "estudios" : "ingenieria",
    "clase social" : "media baja"
}
#ES POSIBLE AGREGAR LISTAS DENTRO DE DICCIONARIOS TAMBIEN   
print (hernan)

#Lo que esta a la izquierda de los dos puntos se llama la llave o clave y por medio de ellos podremos
#acceder a los valores del diccionario

#Para acceder a un valor en particular lo hacemos de la siguiente forma
print("")
print(hernan ["estudios"])

print("")
nombre_completo = hernan ["nombre"] + hernan ["apellido"]
print(f"mi nombre completo es {nombre_completo}") #Esto lo acabo de hacer yo solo, no se como separar hernanherrera que quedo pegado
print("")

#Agregar valor
hernan ["cualidad"] = "el mas inteligente"  #notese que usamos igual

print (hernan)

print("")

# cambiar un valor:
hernan["cualidad"] = "fachero e inteligente"
print(hernan)