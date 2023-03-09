from random import randint 
from matplotlib import pyplot

tiradas = 20  #NÚNEROS DE VECES QUE VA A SIMULAR QUE SE TIRARON LOS DADOS.


#Tirar los dados
def tirar_dados(tiradas):
    for i in range (tiradas):
        dado1= randint(1,6)
        dado2= randint(1,6)
        combinaciones.append(dado1+dado2)
    #print(combinaciones)
    if tiradas<1000:
        print(combinaciones)
    

combinaciones = []
tirar_dados(tiradas)


#Crear tabla de frecuencia
valores_posibles = list(range (2,13)) 
frecuencias_abs = []

for i in valores_posibles:
    contador = 0
    for j in combinaciones:
        if j == i:
            contador= contador+1 
    frecuencias_abs.append(contador)
    print (str(i) + '=' + str(contador))


#Crear grafico
pyplot.title(f'Cantidad de veces que se repiten las combinaciones en {tiradas} tiradas'  )
pyplot.bar(valores_posibles, height= frecuencias_abs, width= 0.5)
pyplot.xticks(valores_posibles)
if (tiradas<=50):
    pyplot.yticks(range(0, max(frecuencias_abs)+1, 1))
elif (tiradas<=200 and tiradas>50):
    pyplot.yticks(range(0, max(frecuencias_abs)+1, 2))
elif (tiradas<=500 and tiradas>200):
    pyplot.yticks(range(0, max(frecuencias_abs)+1, 5))
elif (tiradas<=1500 and tiradas>500):
    pyplot.yticks(range(0, max(frecuencias_abs)+1, 10))
elif (tiradas<=10000 and tiradas>1500):
    pyplot.yticks(range(0, max(frecuencias_abs)+1, 50))

    




pyplot.show()



