def sumaRangoNumeros(numeroMayor, numeroMenor):
    suma = 0
    if numeroMayor<numeroMenor:
        numeroMayor, numeroMenor = numeroMenor, numeroMayor
    for numero in range(numeroMenor, (numeroMayor+1)):
        suma += numero
    
    print(suma)