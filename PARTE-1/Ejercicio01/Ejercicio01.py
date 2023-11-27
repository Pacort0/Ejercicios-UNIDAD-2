from multiprocessing import *
from funciones import *

if __name__ == '__main__':

    p1 = Process(target=sumaHastaMax, args=(7,))
    p2 = Process(target=sumaHastaMax, args=(8,))
    p3 = Process(target=sumaHastaMax, args=(0,))
    p4 = Process(target=sumaHastaMax, args=(3,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    print("Procesos acabaos")

