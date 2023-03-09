# Es posible anidar if´s en el codigo, sin embargo esto no es lo mas conveniente. Ej:
ocupacion = "estudiante"
if ocupacion == "desempleado":
    print("No seas vago man")
else:
    if ocupacion == "estudiante":
        print ("mandale al estudio bro")
    else:
        print("la concha de tu hermana") 


# Esto no es eficaz y en su lugar se usa el comando elif como veremos en el siguiente ej:
edad = "joven"
if edad == "viejo":
    print ("Tomate la pastilla y anda a dormir viejo")
elif edad == "joven":           
    print("sos joven loco")
else:
    print("no sos ni viejo ni joven")
#Se pueden agregar todos los elif que se quiera.



