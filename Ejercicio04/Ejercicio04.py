from funciones import *
from multiprocessing import *

ficheroNumeros = "Ejercicio03//numeros.txt"

if __name__ == '__main__':
    left, right = Pipe()
    p1 = Process(target=sumaHastaMax, args=(left,))
    p2 = Process(target=leeNumeros, args=(ficheroNumeros, right,))

    p1.start()
    p2.start()

    p2.join()
    p1.join()