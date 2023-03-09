#Para introducir datos vamos a utilizar la función "input". ej.

nombre = input("¿cúal es tu nombre?: \r\n")  # \r\n sirve para que salte una linea para poner el input

print(f"Hola {nombre}")

# Cuando ponemos un input el programa siempre lo va a leer como un str, por eso si queremos que sea un entero
# por ejemplo vamos a tener que transformar de str a int. Ej:

edad = input("¿Cuantos años tenes?: \r\n")

edad = int(edad)

if edad >= 18:
    print ("Eres mayor de edad")
else:
    print("Eres menor de edad")