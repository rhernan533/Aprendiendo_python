# and revisa que todas las condiciones sean verdaderas 

sistema_de_representacion = False    
probabilidad = False 
fisica = True
if sistema_de_representacion and probabilidad and fisica:
    print("Felicidades podes cursar 3er año")
else:
    print("Sos un boludo!! tenes que recursar y perder un año, igual vas a ser millonario antes de los 30")

ser_el_mejor = True
apostarlo_todo = True
if ser_el_mejor and apostarlo_todo:
    print("No falta mucho para que lleguen los billetes")
else:
    print("No vale la pena vivir")


usuario_logeado = True
usuario_admin = False
if usuario_admin and usuario_logeado:
    print("Modo administrador")
elif usuario_logeado:
    print("Iniciaste secion como usuario ordinario")
else:
    print("debes iniciar seción")



# Otros operadores son or y xor. 
# El or verifica que por lo menos una de las variables sean verdaderas, o que todas las variables sean verdad
# El xor solo busca que una variable sea verdadera. Si hay mas de una verdadera el xor será falso (no pude
# usarlo jeje).


admin_1 = True
admin_2= False

if admin_1 or admin_2:
    print("Modo administrador")
else: 
    print("no eres administrador")


dinero = True
tarjeta_credito = True

if dinero or tarjeta_credito:
    print("Pudes pagarlo")
else:
    print("No seas croto man")

