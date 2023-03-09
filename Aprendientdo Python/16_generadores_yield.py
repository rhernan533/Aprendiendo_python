#Ahora vamos a ver como yield nos va a permitir guardar de uno en uno cada valor. Esto puede ser mas eficiente
# ya que en siertos casos no sera necesario reservar todos los espacios en memorias señalados.

#Con "yield" el programa guardará de uno en uno los valores 

def num_pares(limite):
    i=1
    while i<= limite:
        yield i*2  # Yield es un objeto que es capaz de retornar sus miembros uno a la vez
        i+=1  

lista_pares = num_pares(10) # <--Cambiar el numero para cambiar la cantidad de n° que genera el programa 
# No podemos hacer esto: print(num_pares(10)) - hay que asignar un objeto donde se guarde los valores de la funcion

print (next(lista_pares))  #luego para acceder a los valores se utiliza la función secuencial next()
print (next(lista_pares))
print (next(lista_pares))
print (next(lista_pares))

