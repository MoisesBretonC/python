diccionario = {'c1':'valor1', 'c2':'valor2', 'c3':'valor3'}
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre':'Moises','apellidos':'Breton','email':'moisesbreton11@gmail.com','peso':87,'talla':1.84}
consulta = (cliente['apellidos'])

print(consulta)

dic = {'1':55,'2':[10,20,30],'3':{'s1':100,'s2':200,'s3':300}}
print(dic['3']['s1'])

dic2 = {'p1':['a','b','c'],'p2':['d','e','f']}
print(dic2['p1'][0].upper())

dic3 = {1: 'a', 2: 'b', 3: 'c'}
print(dic3[1])

dic3 [3] = 'c'

print(dic3)

dic3 [2] = 'B'
print(dic3)

print(dic3.values())
print(dic3.items())