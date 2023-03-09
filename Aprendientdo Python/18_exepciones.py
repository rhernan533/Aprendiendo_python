'''
Las exepciones nos van a permitir que se siga ejecutando nuestro programa aunque salga un error de ejecucion.
Por ejemplo no es posible hacer una divsion por cero, normalmente antes esta situación nos saldria un error
y nuestro programa se dejaria de ejecutar. Sin embargo podemos usar las exepciones para que antes este error
nuestro programa se siga ejecutando y realize la accion que le indiquemos.
Hagamos el ejemplo de la division:'''

def division():
    try:  #"try" y "except" nos van a permitir decirle al programa que hacer ante ciertos errores
        a = float(input("Intoduce el primer valor: "))
        b = float(input("Intoduce el segundo valor: "))
        print ("El resultado es: " + str(a/b))

    except ZeroDivisionError:  #ZeroDivisionError: error al dividir por cero.
       print("No se puede dividir entre cero") 
       
    except ValueError:  #ValueError: error al introducir valores no validos.
        print("No son validos los valores introducidos")
   

division()
print ("Operación finalizada")

''' SI NO ESPECIFICAMOS EL ERROR DESPUES DEL EXCEPT PODEMOS DAR UNA INTRODUCCION AL PROGRAMA PARA TODOS LOS 
ERRORES EN GENERAL''' 

