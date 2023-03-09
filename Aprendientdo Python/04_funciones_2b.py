def funcion2b(nombre="persona no identificada",trabajo = "desconocido"):  #definiremos ahora una funcion con dos parametros  
    print(f"{nombre} trabaja de {trabajo}") 

#El "= desconocido" que le sigue al parametro trabajo es llamado parametro por default, que en caso de no 
#poner un valor a ese parametro no nos saldra error y nos arrojara por resultado el default

funcion2b("Hernán", "ingeniero y empresario")    
funcion2b("Julian", "ingeniero y empleado mas importante de Hernán")
funcion2b("Brisa Conrradi", "puta de Hernán")                    
funcion2b("Nacho")                  
funcion2b()