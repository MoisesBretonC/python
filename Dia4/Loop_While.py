monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
else: print("No tengo mas dinero")


respuestas = "s"
while respuestas == "s":
    break
    respuestas= input("quieres seguir? S/N" )
else:
    print("gracias")



nombre = input("nombre: ")
for  letra in nombre:
    if letra == "a":
        break
    print(letra)

apellido = input("apellido:")
for letra in apellido:
    if letra == "a":
        continue
    print(letra)


