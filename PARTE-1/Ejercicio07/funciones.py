def sumaRangoNumeros(cola):
    numeroMax = cola.get() #Le damos a numeroMax el valor del primer número enviado
    numeroMin = cola.get() #Le damos a numeroMin el valor del segundo número enviado
    while numeroMax or numeroMin is not None: #Mientras ninguno de los dos valores sea none
        suma = 0 
        if numeroMax<numeroMin: #Los ponemos en orden según su valor
            numeroMax, numeroMin = numeroMin, numeroMax
        for numero in range(numeroMin, (numeroMax+1)): 
            suma += numero #Hacemos la suma
        print(suma)
        numeroMax = cola.get() #Cogemos los siguientes valores
        numeroMin = cola.get()


def leeNumeros(nombreArchivo, cola):
    archivo = open(nombreArchivo, "r")
    for linea in archivo:  #Leemos el archivo línea a línea
        for numero in linea.strip().split(' '): #Leemos cada línea sin espacios ni saltos de línea
            cola.put(int(numero)) #Enviamos cada número que leemos
    archivo.close()
    cola.put(None)