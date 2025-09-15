x = True

if x:
    print("Es correcto")

if 5 == 2:
    print("Es correcto")
else:
    print("No es correcto")

mascota = 'perro'
if mascota == 'gato':
    print("El mascota es gato")
elif mascota == "perro":
    print("tienes un perro")
else:
    print("no se que animal tienes")

edad = 17
calificacion = 9
if edad < 18:
    print("El joven es menor")
    if calificacion >=7:
        print("Aprobado")
    else:
        print("reprobado")
else:
    print("El joven es mayor")