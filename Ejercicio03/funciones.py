def sumaHastaMax(cola):
    suma = 0
    numeroMax = cola.get()
    rango = range((int)(numeroMax+1))
    while numeroMax is not None:

        for numero in rango:
            suma+=numero

    cola.put(None)
    print (suma)

   

def leeNumeros(nombreArchivo, cola):
    archivo = open(nombreArchivo, "r")
    numeros = archivo.read()
    for numero in numeros:
        cola.put(numero)
    archivo.close()
    return cola
