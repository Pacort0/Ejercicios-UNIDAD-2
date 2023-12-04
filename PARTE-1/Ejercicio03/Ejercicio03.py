from funciones import *
from multiprocessing import *

ficheroNumeros = "C:/Users/Usuario/Desktop/DAM 2/PSP/Ejercicios_Multiprocessing/Ejercicios-UNIDAD-2/Ejercicios-UNIDAD-2/PARTE-1/Ejercicio03/numeros.txt"

if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=sumaHastaMax, args=(queue,))
    p2 = Process(target=leeNumeros, args=(ficheroNumeros, queue,))

    p1.start()
    p2.start()

    p2.join()
    p1.join()

    print("El acabose")

