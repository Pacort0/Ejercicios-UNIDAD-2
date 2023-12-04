from multiprocessing import *
import random

def procesoGeneraNotas(cantidad, fichero):
    with open(fichero, "w") as archivo:
        for i in range(cantidad):
            num = round(random.uniform(0,10), 2)
            archivo.write(f"{num}\n")

def mediaNota(fichero, nombreAlumno):
    with open(fichero, "r") as archivo:
        suma = 0
        for linea in archivo.readlines():
            nota = float(linea)
            suma += nota
        media = suma/6
    with open("medias.txt", "a") as medias:
        medias.write(f"{media}{nombreAlumno}\n")

if __name__ == "__main__":
    for i in range(10):
        proceso1 = Process(target=procesoGeneraNotas, args=(10, f"Alumno{i+1}.txt"))
        proceso1.start()
    
    for i in range(10):
        proceso2 = Process(target=mediaNota, args=(f"Alumno{i+1}.txt", f"Alumno{i+1}"))
        proceso2.start()
    
