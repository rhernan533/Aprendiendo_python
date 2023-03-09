#Preguntas:
#¿1110+90 es igual a 2000?
#¿8x8 es igual 64?
#¿Cordoba es la capital de Argentina?
participante = input("¿Cual es tu nombre? \r\n")
print(f"Hola {participante}. \r\nCompleta el examen con V (verdadero) o F (falso). Al terminar el examen se le asigara una nota. \r\nSerá necesario una nota minima de 2 para aprobar")

aprobado = True

print("Pregunta 1: ¿1110+90 es igual a 2000?  ")
respuesta1 = input()
respuesta_min1 = respuesta1.lower() #en caso de que el usuario conteste en mayuscula, este codigo lo 
print("Pregunta 2: ¿8x8 es igual 64?  ")
respuesta2 = input()
respuesta_min2 = respuesta2.lower() #convertira a  miniscular para que luego en los if el programa no lo 
print("Pregunta 3: ¿Cordoba es la capital de Argentina?  ")
respuesta3 = input()
respuesta_min3 = respuesta3.lower()   # tome como falso por mas que las respuestas sean correctas.

puntaje = 0
if respuesta_min1 == "f":    #Otra opcion podria ser haber agragado un or: f or F
    puntaje = puntaje + 1  
if respuesta_min2 == "v":   
    puntaje = puntaje + 1   
if respuesta_min3 == "f":
    puntaje = puntaje + 1   
  
print (f"Su punaje obtenido fue {puntaje}")

if puntaje >= 2:
    print ("Felicitaciones, Aprobó!")
else:
    print("La nota es insuficiente. Intentelo de nuevo")