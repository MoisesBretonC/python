nombre = ['juan','Maria','jose']

for elemento in nombre:
    numero_letra = nombre.index(elemento) + 1
    print(f"hola bola {numero_letra}: {elemento}")

lista = ['Paco','Pedro','Martha','Moises']
for nombre in lista:
    if nombre.startswith('M'):
        print(nombre)
    else:
        print('nombre que comienza con L')

numeros = [1,2,3,4,5,6,7,8,9]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor)


dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.items():
    print(item)