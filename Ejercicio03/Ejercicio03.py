from funciones import *
from multiprocessing import *

ficheroNumeros = "Ejercicio03//numeros.txt"

if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=sumaHastaMax, args=(queue,))
    p2 = Process(target=leeNumeros, args=ficheroNumeros)

    p1.start()
    p2.start()

    queue.put(p2.join())
    p1.join()

