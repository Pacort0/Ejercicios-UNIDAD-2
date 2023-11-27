def sumaHastaMax(cola):
    numeroMax = cola.get() #numeroMax toma el primer valor de la cola
    while numeroMax is not None: #Mientras el elemento en la cola no sea None 
        rango = range(int(numeroMax+1)) #Creamos un rango que vaya desde 1 hasta numeroMax+1
        suma = 0 #Declaramos la variable suma = 0
        for numero in rango: #Recorremos el rango de números
            suma+=numero #Incrementamos la suma
        print (suma) #Mostramos el resultado
        numeroMax = cola.get() #Cogemos el siguiente valor de la cola
        

   

def leeNumeros(nombreArchivo, cola):
    archivo = open(nombreArchivo, "r")
    for numero in archivo:  #Leemos el archivo línea a línea
        cola.put(int(numero.strip())) #Strip() ignora los espacios en blanco al principio y al final de la línea, incluyendo el salto de línea
    archivo.close()
    cola.put(None)
