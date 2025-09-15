nombres = ["Juan", "Pedro", "Moises"]
edades = [35, 45, 24]
ciudades = ['mexico', 'madrid', 'buenos aires']

combinados = list(zip(nombres, edades, ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")