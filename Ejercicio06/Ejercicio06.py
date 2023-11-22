from multiprocessing import *
from funciones import *

if __name__ == '__main__':
    with Pool(processes=3) as piscina:
        numbers = [(8, 4), (16,3), (20, 50), (50,25)] #Mandamos varias tuplas dentro de una misma tupla
        results = piscina.starmap(sumaRangoNumeros, numbers)
    
    print("Resultados", results)