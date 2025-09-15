from random import *

#escoge un numero al azar entre el 1 al 100
aleatorio = randint(1,100)
print(aleatorio)

#escoge un numero de entre 1 al 5 pero en decimal
aleatorio2 = round(uniform(1,5),1)
print(aleatorio2)

#escoge entre un numero 1 o 0 con decimales aleatoriamente
aleatorio3 = random()
print(aleatorio3)

#escoge un valor entre una lista
colores= ['azul','rosa','verde']
aleatorio4 = choice (colores)
print(aleatorio4)

#escoge un numero entre el rango que tu elijas y lo adjunta en una lista de manera aleatoria
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)