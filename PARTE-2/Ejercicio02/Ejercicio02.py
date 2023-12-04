from multiprocessing import *
from random import *
from multiprocessing.connection import PipeConnection

ficheroNumeros = "Ejercicio03//numeros.txt"

def procesoGeneraIp(direcciones, tuberia:PipeConnection):
    ip=""
    for direccion in range(direcciones):
        for _ in range(4):
            ip += str(randint(0, 255))
            if _ != 3:
                ip+="."
        else:
            tuberia.send(ip)
            ip=""
    tuberia.send(None)

def procesoFiltraABC(tubleft:PipeConnection, tubright:PipeConnection):
    ip = tubleft.recv()
    while ip is not None:
        octetos = ip.split(".")
        octeto1 = int(octetos[0])
        if octeto1<=223:
            tubright.send(ip)
        
        ip = tubleft.recv()
    tubright.send(None)
    
    
def procesoResultado(tuberia:PipeConnection):
    ip = tuberia.recv()
    while ip is not None:
        octetos = ip.split(".")
        octeto1 = int(octetos[0])
        if octeto1 <= 127:
            print(ip, "Clase A")
        elif octeto1 <= 191:
            print(ip, "Clase B")
        elif octeto1 <= 223:
            print(ip, "Clase C")

        ip = tuberia.recv()

if __name__ == '__main__':
    left1, right1 = Pipe()
    left2, right2 = Pipe()

    p1 = Process(target=procesoGeneraIp, args=(10,left1))
    p2 = Process(target=procesoFiltraABC, args=(right1, left2))
    p3 = Process(target=procesoResultado, args=(right2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Procesos finalizados")
