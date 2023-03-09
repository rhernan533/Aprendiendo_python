#Función maximo -> Dados dos numeros la funcion debe encontrar cual es el mas grande y retornarlo .
#Tambien debe coprobar que los argumentos ingresados sean de tipo float o int, de lo contrario devolver false

def numero_mayor(a,b):
    if (type(a)== float or type(a)== int) and (type(b)== float or type(b)==int):
        if a-b < 0:
             print(f"{b} es mayor que {a} ")
        elif a-b > 0:
            print(f"{a} es mayor que {b} ")
        else:
            print(f"Los números ingresados son iguales: {a} = {b}")
    else:
        print("ERROR: Se deben ingresar datos de tipo numerico")
        return False

numero_mayor(6,6)
        