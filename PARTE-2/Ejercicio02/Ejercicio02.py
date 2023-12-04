from multiprocessing import *
from random import *
from multiprocessing.connection import PipeConnection

ficheroNumeros = "Ejercicio03//numeros.txt"

def procesoGeneraIp(tuberia:PipeConnection):
    ip=""
    for _ in range(4):
        ip += str(randint(0, 255))
        if _ != 3:
            ip+="."
    else:
        tuberia.send(ip)

def procesoFiltraABC(tubleft:PipeConnection, tubright:PipeConnection):
    ip = tubleft.recv()
    if ip.startswith("10."):
        tubright.send([ip, "A"])
    elif ip.startswith("172."):  
        partes = ip.split(".")
        if 16 <= int(partes[1]) <= 31: #Si el valor dentro de partes[1] está entre 16 y 31
            tubright.send([ip, "B"])
    elif ip.startswith("192.168"):
        tubright.send([ip, "C"])
    else:
        tubright.send([ip, "Ninguno"])
    
    
def procesoResultado(tuberia:PipeConnection):
    print(tuberia.recv())

if __name__ == '__main__':
    left1, right1 = Pipe()
    left2, right2 = Pipe()

    for _ in range(100):
        p1 = Process(target=procesoGeneraIp, args=([left1]))
        p2 = Process(target=procesoFiltraABC, args=([right1, left2]))
        p3 = Process(target=procesoResultado, args=([right2]))

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()

    print("Procesos finalizados")
