from multiprocessing import *
import random
import time

def procesoGeneraNotas(cantidad, fichero):
    with open(fichero, "w") as archivo: 
        for i in range(cantidad): #Creamos X numeros random y los escribimos en el archivo
            num = round(random.uniform(0,10), 2)
            archivo.write(f"{num}\n")

def mediaNota(fichero, nombreAlumno):
    with open(fichero, "r") as archivo: 
        suma = 0
        for linea in archivo.readlines(): #Calculamos la media de las notas del alumno
            nota = float(linea)
            suma += nota
        media = suma/6
    with open("medias.txt", "a") as medias:
        #Escribimos la media y el nombre del alumno en el fichero
        medias.write(f"{round(media, 2)} {nombreAlumno}\n")

def notaMax():
    notaMax = 0.0
    nombreAlumno = ""
    with open("medias.txt", "r") as medias:
        for _ in medias.readlines(): #Leemos el fichero por lineas
            linea = _.split(" ") #Separamos por espacios
            if float(linea[0]) > notaMax: #Si la nota leida es mayor a la guardada
                notaMax = float(linea[0]) #La nota máxima pasa a ser esa
                nombreAlumno = linea[1] #El nombre del alumno que ha sacado la nota se guarda
        print("Nota máxima =",notaMax,"Alumno =", nombreAlumno)




if __name__ == "__main__":

    inicio=time.time()

    procesos1=[]
    procesos2=[]

    for i in range(10):
        proceso1 = Process(target=procesoGeneraNotas, args=(6, f"Alumno{i+1}.txt"))
        proceso1.start()
        procesos1.append(proceso1)

    for p in procesos1:
        p.join()

    
    for i in range(10):
        proceso2 = Process(target=mediaNota, args=(f"Alumno{i+1}.txt", f"Alumno{i+1}"))
        proceso2.start()
        procesos2.append(proceso2)

    for p in procesos2:
        p.join()

    p3=Process(target=notaMax())
    p3.start()
    p3.join()
    
