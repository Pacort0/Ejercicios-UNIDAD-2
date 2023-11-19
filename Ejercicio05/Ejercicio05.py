from funciones import *
from multiprocessing import *

if __name__ == '__main__':

    p1 = Process(target=sumaRangoNumeros, args=[-2,7])
    p2 = Process(target=sumaRangoNumeros, args=[8, 4])
    p3 = Process(target=sumaRangoNumeros, args=[20, 30])
    p4 = Process(target=sumaRangoNumeros, args=[0, -4])

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    print("Procesos acabaos")