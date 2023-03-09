limite_contador = int(input("Contador de capicuas- INGRESE UN NÚMERO-> "))

def cont_capicua(limite_contador):
    capicuas = []
    cont = 0
    for i in range(limite_contador + 1): #Es NECESARIO poner range porque un int no es un objeto iterable, una lista si.
        if len(str(i)) >= 2:
            num_reves = str(i)[::-1]
            if num_reves == str(i):
                cont = cont + 1
                capicuas.append(i)
    print(capicuas)  
    print (f"\r\nHay {cont} números capicuas en el intervalo (0, {limite_contador})")
            
                         
cont_capicua(limite_contador)

