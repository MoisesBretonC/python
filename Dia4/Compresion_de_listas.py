
#concepto de lista normal
palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

#metodo acortado
palabra2 = 'JavaScript'
lista2 = [letra2 for letra2 in palabra2]
print(lista2)

#metodo acortado pero con numeros
lista3 = [n for n in range(0,21,2)]
print(lista3)

#metodo para dividir en 2 el numero
lista4 = [n / 2 for n in range(0,30,2)]
print(lista4)

#este es para saber si un numero multiplicado x2 es mayor que 10
lista5 = [n for n in range(0,80,2) if n *2 > 10]
print(lista5)


#este es para saber si un numero multiplicado x2 es mayor que 10 pero aqui se añade un else 
lista5 = [n if n *2 > 10 else "no" for n in range(0,80,2) ]
print(lista5)

#este es  para dividir
pies = [10,20,30,40,50]
metros = [p/3.281 for p in pies]
print (metros)