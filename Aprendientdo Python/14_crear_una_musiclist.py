musiclist = {}  #comenzamos por un diccionario vacio que el usuario irá completando
musiclist ["canciones"] = [] #definimos una lista dentro de la musiclist donde iran las canciones
def app(): 
    musiclist ["nombre_musiclist"] = input ("¿Cómo desea llamar su musiclist?:  ")
    while not musiclist ["nombre_musiclist"]: #en Python un string vacio se evalua como False///Tambien se pudo usar: while musiclist ["nombre_musiclist"] == ""
         print ("\r\nDebes ponerle un nombre a tu musiclist")
         musiclist ["nombre_musiclist"] = input ("Ingrese un nombre para su musiclist:  ")
    
    agregar_canciones()

def agregar_canciones ():
    nombre= musiclist ["nombre_musiclist"]
    agregar_canciones = True
    while agregar_canciones:
        canciones = input (f"\r\n¿Qué cancion desea agregar a la musiclist {nombre}?\r\n(Escriba ´x´ para dejar de agregar canciones):\r\n")  
        if canciones == "x" or canciones == "X":
            agregar_canciones = False
        else:
          musiclist ["canciones"].append(canciones) #Con .append es que se agrega elemento a una lista
          print (musiclist)
 
app()
nombre = musiclist ["nombre_musiclist"]
print (f"Su musiclist es: {nombre}\r\nCanciones de {nombre}:")
for cancion in musiclist ["canciones"]:
    print (cancion)

#COSAS QUE NO RECORDABA HASTA QUE HICIMOS ESTO:
#EL .APPEND PARA AGREGAR COSAS A LA LISTA
#LO DE FOR...IN...; ESO DEFINITIVAMENTE NO ME ACORDABA, VER DE NUEVO 