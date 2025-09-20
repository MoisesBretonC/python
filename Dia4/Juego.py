from random import *

#aqui estamos haciendo la variable de intentos que es igual a 0
#manejar la variable como 0 en este porque solo se almacena un valor numerico
intentos = 0
estimado = 0
nombre = input('Ingrese su nombre: ')
#aqui estamos haciendo que se escoja un numero de entre 1 y 100 y se almacene en la variable numero_aleatorio
numero_aleatorio = randint(1,100)
print(f"Hola {nombre} he pensando en un numero entre 1 y 100, tienes 8 intentos para adivinar el numero")

#aqui estamos diciendo que mientras intentos sea menor que 8 todavia tenemos vidas
while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    #aqui vamos añadiendo un intento mas, osea vamos perdiendo una vida
    intentos += 1
    #aqui esta haciendo que el if haga que nomas tenga numeros del 1 al 100
    if estimado not in range(1,101):
        print("El numero que ingresaste no se puede usar ")
    elif estimado < numero_aleatorio:
        print("mi numero es mas alto")
    elif estimado > numero_aleatorio:
        print("mi numero es menor")
    #aqui  iba esto if estimado == numero_aleatorio: pero lo vamos a sustituir por un else
    else:
        print(f"felicidades {nombre} has encontrado el numero {numero_aleatorio} en tu intento {intentos}")
        break

if estimado != numero_aleatorio:
    print(f"lo siento se acabaron los intentos, el numero secreto era {numero_aleatorio}")

