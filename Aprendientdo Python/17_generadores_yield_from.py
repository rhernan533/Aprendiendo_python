# TRES COMILLAS SIMPLES PARA COMENTARIO MULTI-LINEA 

'''  CODIGO 1: Yield normal- devuelve lista de provincias solicitadas de una region
noa = ("Corrientes", "Misiones", "Chaco")
nea = ("Jujuy", "Salta", "Tucuman")
patagonia = ("Tierra del Fuego", "Rio negro", "Chubut")

def provincias(*regiones):#Cuanndo ponemos un asterisco es para indicar al programa que no hay un numero especifico de variables que vamos a ingresar
    for integrantes in regiones:
     yield integrantes

prov_regiones = provincias(noa, nea, patagonia, nea)     

print (next(prov_regiones))
print (next(prov_regiones))
'''

#Esté es un yield comun que nos devuelve unicamente las prov del nea y noa por que solo usamos "dos next" 


#Ahora vamos a ver si podemos hacer que nos devuelva solo las proviencias y no la lista completa
#Para hacerlo, si no existiera la funcion "yield from", deberiamos usar un bucle de dos "for". 
#Estará comentado como seria si tuviesemos que usar dos "for".

noa = ("Corrientes", "Misiones", "Chaco")
nea = ("Jujuy", "Salta", "Tucuman")
patagonia = ("Tierra del Fuego", "Rio negro", "Chubut")

'''  CODIGO 2: Yield con for anidados- devuelve provincias solicitadas de una o mas regiones

def provincias(*regiones):
    for integrantes in regiones:
        for provincia in integrantes:
         yield provincia  

prov_regiones = provincias(noa, nea, patagonia)     

print (next(prov_regiones))
print (next(prov_regiones))
'''

# En este codigo haremos un programa igual al del CODIGO 2 pero sin usar for anidados, sino usando yield from

# Las regione ya estan definidas arriba 

def provincias(*regiones):
    for integrantes in regiones:
         yield from integrantes  

prov_regiones = provincias(noa, nea, patagonia)     

print (next(prov_regiones))
print (next(prov_regiones))


