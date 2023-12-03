from multiprocessing import *
from random import *
from multiprocessing.connection import PipeConnection

ficheroNumeros = "Ejercicio03//numeros.txt"

def procesoGeneraIp(numeroIPs, tuberia:PipeConnection):
    ips = []
    for ip in range(numeroIPs):
        ip=""
        for _ in range(4):
            ip += str(randint(0, 255))
            if _ != 3:
                ip+="."
            else:
                ips.append(ip)
        else:
            tuberia.send(ips)

def procesoFiltraABC(tubleft:PipeConnection, tubright:PipeConnection):
    ips = tubleft.recv()
    for ip in ips:
        if ip.startswith("10."):
            tubright.send([ip, "A"])
        elif ip.startswith("172."):  
            partes = ip.split(".")
            if 16 <= partes[1] <= 31: ##Si el valor dentro de partes[1] está entre 16 y 31
                tubright.send([ip, "B"])
        elif ip.startswith(192.168):
            tubright.send([ip, "C"])
        else:
            tubright.send([ip, "Ninguno"])
    
    
def procesoResultado(tuberia:PipeConnection):
    ips = tuberia.recv()
    for ip in ips:
        print("Dirección:", ip)


if __name__ == '__main__':
    left, right = Pipe()
    p1 = Process(target=procesoGeneraIp, args=([10, left]))
    p2 = Process(target=procesoFiltraABC, args=([left, right]))
    p3 = Process(target=procesoResultado, args=([right]))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Procesos finalizados")
