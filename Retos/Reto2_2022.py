 # Reto #2
 # LA SUCESIÓN DE FIBONACCI
 # Fecha publicación enunciado: 10/01/22
 # Fecha publicación resolución: 17/01/22
 # Dificultad: DIFÍCIL
 #
 # Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci
 # empezando en 0.
 # La serie Fibonacci se compone por una sucesión de
 # números en la que el siguiente siempre es la suma de los dos anteriores.
 # 0, 1, 1, 2, 3, 5, 8, 13...


#Se va repetir solo 50 Veces.
def fibonacci(catidadVeces):
    inicio = 0
    numAnterior = 0
    numSiguiente = 1
    suma = 0
    for inicio in range(cantidadVeces):
        if inicio == 0:
            print (f"{numAnterior}, {numSiguiente}, ",end="")
        else:
            suma = numAnterior + numSiguiente
            print (f"{suma}, ",end="")
            numAnterior = numSiguiente
            numSiguiente = suma

cantidadVeces = 49
fibonacci(cantidadVeces)
        
    
  
        