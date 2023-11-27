from multiprocessing import *


#comparten una misma cola (ejemplo de cola explicado en clase: Fifo->First in first out)

def productor(cola):
    #leer los rangos por cada numero
    for i in range (1,11):
        #añademos el elemento en la variable cola
        cola.put(i)
    #he terminado de meter cosas en la cola
    cola.put(None)
    

def consumidor(cola):
    #obtiene el elemento de la cola
    objeto =cola.get()
    #va leyendo los valores
    while objeto is not None:
        #se imprime el numero que ha obtenido
        print(objeto)
        #se cambia el valor al siguiente
        objeto=cola.get()








if __name__=="__main__":
    queue=Queue()
    p1=Process(target=productor,args=(queue,))
    p2=Process(target=productor,args=(queue,))

    p1.start()
    p2.start()

    p1.join()

    p2.join()
    print("Se terminaron los procesos.")