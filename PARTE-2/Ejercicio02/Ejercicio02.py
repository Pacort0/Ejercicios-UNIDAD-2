from multiprocessing import *
from funciones import *
from multiprocessing.connection import PipeConnection

ficheroNumeros = "Ejercicio03//numeros.txt"

def generateIp(numeroIPs, tuberia:PipeConnection):
    for ip in range(numeroIPs):
        ip=""
        for _ in range(4):
            ip += str(randint(0, 255))
            if _ != 3:
                ip+="."
        else:
            tuberia.send(ip)

def filtraABC(tubleft:PipeConnection, tubright:PipeConnection):
    ip = tubleft.recv()
    

if __name__ == '__main__':
    generateIp(10)