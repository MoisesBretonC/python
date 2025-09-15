nombre = input("Cual es tu nombre: ")
ventas = int (input("cuanto es el total de tus ventas: "))

comision = round(ventas * 13/ 100,2)


input(f"hola {nombre} tu comision es {comision} ")