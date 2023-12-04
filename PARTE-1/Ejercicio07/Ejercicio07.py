from funciones import *
from multiprocessing import *

ficheroNumeros = "numeros.txt"

if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=sumaRangoNumeros, args=(queue,))
    p2 = Process(target=leeNumeros, args=(ficheroNumeros, queue,))

    p1.start()
    p2.start()

    p2.join()
    p1.join()