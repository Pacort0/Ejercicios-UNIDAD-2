from random import *

def generateIp(numeroIPs, conn):
    for ip in numeroIPs:
        for _ in range(4):
            ip += str(randint(0, 255)) + "."
        conn.send(ip)
    conn.send(None) 

def filtraIp(right1, left2):
    ip = right1.recv()
    while ip is not None:
        partes = ip.split(".")
        parte = partes[]
