def sumaRangoNumeros(conn):
    numeroMax = conn.recv() #Le damos a numeroMax el valor del primer número en la cola
    numeroMin = conn.recv() #Le damos a numeroMin el valor del segundo número en la cola
    while numeroMax or numeroMin is not None: #Mientras ninguno de los dos valores sea none
        suma = 0 
        if numeroMax<numeroMin: #Los ponemos en orden según su valor
            numeroMax, numeroMin = numeroMin, numeroMax
        for numero in range(numeroMin, (numeroMax+1)): 
            suma += numero #Hacemos la suma
        print(suma)
        numeroMax = conn.recv() #Cogemos los siguientes valores enviados
        numeroMin = conn.recv()


def leeNumeros(nombreArchivo, conn):
    archivo = open(nombreArchivo, "r")
    for linea in archivo:  #Leemos el archivo línea a línea
        for numero in linea.strip().split(' '): #Leemos cada línea sin espacios ni saltos de línea
            conn.send(int(numero)) #Añadimos cada número a la cola
    archivo.close()
    conn.send(None)