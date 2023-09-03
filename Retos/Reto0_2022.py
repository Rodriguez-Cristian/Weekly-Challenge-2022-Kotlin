# * Reto #0
# * EL FAMOSO "FIZZ BUZZ"
# * Fecha publicación enunciado: 27/12/21
# * Fecha publicación resolución: 03/01/22
# * Dificultad: FÁCIL
# * Enunciado: Escribe un programa que muestre por consola (con un print) 
#   los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), 
#   sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#Ciclo del 1 al 100
for i in range (100): 
    x = i+1
    # Muestro por consola  
    if ((x % 3) == 0 and (x % 5) == 0 ): #multiplo de 3 y de 5
         print("fizzbuzz")  
    elif ((x % 3) == 0):#multiplo de 3
         print("buzz")
    elif ((x % 5) == 0): # multiplo de 5 
        print("fizz") 
    else:
        print(x)
    