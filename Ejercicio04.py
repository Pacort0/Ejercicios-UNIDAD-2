from multiprocessing import *

def enviaPelis(anioPeli, cola:Queue):
    with open("peliculas.txt") as archivo:
        for linea in archivo.readlines(): #leemos el archivo por líneas
            linea = linea.split(";") #quitamos el salto de línea de 
            if str(linea[1].strip()) == (str(anioPeli)): #Si el año de la pelicula coincide con el pasado por parámetros
                cola.put(linea[0]) #Ponemos el nombre de la pelicula en la cola
        cola.put(None) #Ponemos None para indicar que se han acabado las iteraciones

def ficheroPorAnio(anioPeli, cola:Queue):
    pelicula = cola.get() #Recogemos lo último introducido en la cola
    while pelicula != None: #mientras lo introducido en la cola no sea 'none'
        with open(f"Peliculas{anioPeli}.txt", "a") as archivoPelis:
            archivoPelis.write(f"{pelicula}\n") #Escribimos la pelicula en el archivo correspondiente

        pelicula = cola.get() #Cogemos la siguiente pelicula de la cola

if __name__ == "__main__":
    queue = Queue()
    anio = 2019

    p1 = Process(target=enviaPelis, args=(anio, queue))
    p2 = Process(target=ficheroPorAnio, args=(anio, queue))

    p1.start()
    p2.start()
  
    p1.join()
    p2.join()
        