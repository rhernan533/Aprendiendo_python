class Restaurantes:

    def __init__(self,nombre, mejor_plato, precio):
        self.nombre = nombre
        self.mejor_plato = mejor_plato
        self.precio = precio

    def datos_restaurantes(self):
        print(f'Nombre: {self.nombre}, Mejor plato: {self.mejor_plato}, Precio: {self.precio}')


restaurant_1 = Restaurantes('Caserito', 'Ravioles', 350)
#El metodo "__init__" hace que la funcion se ejecute sin la necesidad de llamarla
restaurant_1.datos_restaurantes()  #Como esto es un metodo "normal" lo tenemos que llamar para que se ejecute

restaurant_2= Restaurantes('El Italiano', 'Pizza Napolitana', 550)
restaurant_2.datos_restaurantes()

restaurant_3= Restaurantes('El Parrillon', 'Choripan', 440)
restaurant_3.datos_restaurantes()


