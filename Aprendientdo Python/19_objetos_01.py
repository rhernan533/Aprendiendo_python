class Restaurant:   # Definimos una clase
  
    def agregar_nombre(self, nombre): # Esto es un metodo: Es decir una funcion dentro de una clase

        self.hh = nombre       #Esto es un atributo
  # No entendí bien que funcion cumple el: "send." que se encuentra antes de hh, pero es necesario

    def mostrar_informacion(self):    # Se las define igual que a una funcion
            print(f'Nombre: {self.hh}')    

restaurant = Restaurant()
restaurant.agregar_nombre ("Pizzeria HH") #Para llamar un metodo usamos esta estructura
restaurant.mostrar_informacion()

# Que es self todavia no lo entendí bien xD pero ya lo vamos a entender.

# A esto se lo llama paradigma de programacion orientada a objetos. Y nos va a permitir agrupar en una clase definida varios objetos
# como en este caso pueden ser nombre de restaurantes. 

restaurant2 = Restaurant()
restaurant2.agregar_nombre ("Pancheria GR")  
restaurant2.mostrar_informacion()

