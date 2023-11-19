def sumaHastaMax(numeroMax):
    suma = 0
    rango = range(numeroMax+1)
    while True:

        for numero in rango:
            suma+=numero
        
        return suma
   

def leeNumeros(nombreArchivo):
    archivo = open(nombreArchivo, "rt")
    numeros = archivo.readline()
    archivo.close()
    return numeros
