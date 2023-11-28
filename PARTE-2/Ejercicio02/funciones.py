from random import *

def generateIp(numeroIPs, conn):
    for ip in numeroIPs:
        for _ in range(4):
            ip += str(randint(0, 255)) + "."
        conn.send(ip)
    conn.send(None) 


