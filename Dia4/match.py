serie = "N-02"

"""if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Chaifon")
elif serie == "N-03":
    print("Huawei")
else:
    print("No hay nadota")"""

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("motorola")
    case "N-03":
        print("Huawei")
    case _:
        print("No hay nadota")

cliente = {'nombre':"Moises",
           "edad": 45,
           "ocupacion": "chambeador"
           }
pelicula = {'titulo': 'Mad Max',
            'ficha tecnica':{'protagonista':'Keanu Reeves',
                             'director':'Guillermo'}}

elementos = [cliente, pelicula,"libro"]

for e in elementos:
    match e:
        case{'nombre':nombre,
             'edad': edad,
             'ocupacion': ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo':titulo,
              'ficha tecnica':{'protagonista':protagonista,
                               'director':director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto")
