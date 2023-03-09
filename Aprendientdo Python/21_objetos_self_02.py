
class Perro:  #Clase
    ladra = False   #Atributo de la clase

    # Metodo de la clase:
    def crear_perro(self):   
        print ('Se creó un perro')
    
    def ladrar (self):
        self.ladra = True     # Usar "self.ladra" quiere decir que accedemos al atributo ladra de la clase.
#Si solo usamos: "ladra = True", ladra se leera como una variable de el metodo "ladrar". Con self indicamos que
#se modifique a si mismo. 

    
perro1 = Perro()
perro1.crear_perro()  #NO TE OLVIDES LOS PARENTESISSSS
print (perro1.ladra)   # "perro1.ladra" quiere decir que accedemos al atributo "ladra" del objeto "perro1"
perro1.ladrar()
print (perro1.ladra)