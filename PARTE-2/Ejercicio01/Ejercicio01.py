from multiprocessing import *

ficheroCaracteres = "Ejercicio01//vocales.txt"

def leeCaracteres(vocal):
    cantidadVocal = 0
    with open(ficheroCaracteres, "r") as nombreArchivo:
        letras = nombreArchivo.read()
        cantidadVocal = letras.count(vocal)
    
    return cantidadVocal

if __name__ == '__main__':
    with Pool(5) as piscina:
        vocales = ["a", "e", "i", "o", "u"]
        results = piscina.map(leeCaracteres, vocales)  
    print("Resultados", results)