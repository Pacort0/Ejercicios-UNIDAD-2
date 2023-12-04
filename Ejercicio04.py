from multiprocessing import *

def enviaPelis(anioPeli, cola:Queue):
    with open("peliculas.txt") as archivo:
        for linea in archivo.readlines():
            linea = linea.split(";")
            if str(linea[1].strip()) == (str(anioPeli)):
                cola.put(linea[0])
        cola.put(None)

def ficheroPorAnio(anioPeli, cola:Queue):
    pelicula = cola.get()
    while pelicula != None:
        with open(f"Peliculas{anioPeli}.txt", "a") as archivoPelis:
            archivoPelis.write(f"{pelicula}\n")

        pelicula = cola.get()

if __name__ == "__main__":
    queue = Queue()
    anio = 2019

    p1 = Process(target=enviaPelis, args=(anio, queue))
    p2 = Process(target=ficheroPorAnio, args=(anio, queue))

    p1.start()
    p2.start()
  
    p1.join()
    p2.join()
        