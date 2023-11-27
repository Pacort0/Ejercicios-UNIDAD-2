def sumaHastaMax(conn):
    numeroMax = conn.recv() #numeroMax toma el primer valor que se ha mandado
    while numeroMax is not None: #Mientras el elemento enviado no sea None 
        rango = range(int(numeroMax+1)) #Creamos un rango que vaya desde 1 hasta numeroMax+1
        suma = 0 #Declaramos la variable suma = 0
        for numero in rango: #Recorremos el rango de números
            suma+=numero #Incrementamos la suma
        print (suma) #Mostramos el resultado
        numeroMax = conn.recv() #Cogemos el siguiente valor enviado
        

   

def leeNumeros(nombreArchivo, conn):
    archivo = open(nombreArchivo, "r")
    for numero in archivo:  
        conn.send(int(numero.strip())) #Strip() ignora los espacios en blanco al principio y al final de la línea, incluyendo el salto de línea
    archivo.close()
    conn.send(None)
