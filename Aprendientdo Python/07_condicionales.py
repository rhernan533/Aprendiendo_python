# Un condicional permite que el codigo se ejecute teniendo en cuenta ciertas condiciones. Veremos el condi-
#cional if...elf

dinero = 500
if dinero < 700:
    print ("No puedes comprar el producto")
#El ejemplo está enfocado en que queremos compar algo que vale 700 pesos pero solo tenemos 500

#Comunmente usaremos para las condiciones los signo: >(mayor a); >=(mayor o igual a); <(menor a); 
# <=(menor o igual a); ==(igual a); y para decir diferente a, usaremos la palabra "not" despues del if como
#veremos

#Ej 2:
if dinero >= 500:
    print("felicitaciones por tu compra")
else:                    #nos fijamos que "sacamos" la sangria para el else
    print("No tienes el dinero suficiente")    


#Estos operadores (no se si se los puede llamar así xD) tambien se los puede utilizar con los str y booleanos

#Ej 3:
Chica = "Brisa Conrradi"
if Chica == "Brisa Conrradi":
    print("Esa es una trolita")
else:
    print ("hay que conocerla bien") 

Chica2 = "Valeria Castro"
if not Chica2 == "Valeria Castro":
    print("hay que conocerla bien")
else:
    print ("Hay que darle una buena cogida")


#Ej booleano:

atleta_futbol = True
if atleta_futbol:   #con buleanos no es necesario poner: si tal cosa es true, hacer tal cosa. el lenguaje ya verifica para el caso de la variable sea verdadero
    print("vos jugas futbol")
else:
    print("no seas trolo man")

atleta_voley = True
if not atleta_voley:   #Si ponemos "not" va a verificar para el caso que la variable sea igual a falso
     print("vos jugas no jugas voley")
else:
    print("no seas trolo man")
