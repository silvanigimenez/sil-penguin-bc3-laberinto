#creamos un archivo nuevo
#guardamos en la carpeta del repositorio
#con la extension .py
#uso de numeros aleatorios

#importamos la libreria randint
from random import randint
aleatorio=randint(0,20)             #creamos una variable
#y generamos un numero aleatorio entre 0 y 20
print(aleatorio)           #imprimimos el numero generado

#ejercicio
#escribir una funcion sorteo() que reciba
#una lista de participantes, y elegir a uno
#de los participantes aleatoriamente y retornar
#esa persona elegida
#desafio: no volver a retornar una persona
#ya sorteada

from random import randint  #importamos randing de una libreria randint
def sorteo_entradas(Lista_participantes): #definimos una funcion
    cant=len(Lista_participantes)-1     #utilizamos len() para saber la cantidad de personas que hay en la lista para que no salga de rango
    indice=randint(0,cant)              #generamos un indice aleatorio
    ganador=Lista_participantes[indice]  #seleccionamos un elemento de la lista y guardamos en la variable ganador
    return ganador                         #retornamos un ganador
    print(ganador)                         #esto no se ejecuta
Lista_participantes=["Ana","Laura","David","Chew","Silvi"] #creamos una lista
ganar=sorteo_entradas(Lista_participantes)    #llamamos a la funcion y guardamos en una variable el resultado retornado por la funcion
print(ganar)                                #imprimir el ganador



    


 
