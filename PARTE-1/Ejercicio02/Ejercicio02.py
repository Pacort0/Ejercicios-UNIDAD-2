from multiprocessing import *
from funciones import *

if __name__ == '__main__':
    with Pool(processes=3) as piscina:
        numbers = [8, 16, 20, 50]
        results = piscina.map(sumaHastaMax, numbers)
    
    print("Resultados", results)