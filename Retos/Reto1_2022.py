 # Reto #1
 # ¿ES UN ANAGRAMA?
 # Fecha publicación enunciado: 03/01/22
 # Fecha publicación resolución: 10/01/22
 # Dificultad: MEDIA
 #
 # Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean)
 # según sean o no anagramas.
 # Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 # NO hace falta comprobar que ambas palabras existan.
 # Dos palabras exactamente iguales no son anagrama.
 
#Función 
 

def son_anagramas(palabra1, palabra2):
    
    # Eliminar espacios en blanco y convertir las palabras a minúsculas
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # Verificar si las longitudes de las palabras son diferentes
    if len(palabra1) != len(palabra2):
        return False

    # Contar la frecuencia de cada letra en ambas palabras
    frecuencia_palabra1 = {}
    frecuencia_palabra2 = {}
    
   
    for letra in palabra1:
        if letra in frecuencia_palabra1:
            frecuencia_palabra1[letra] += 1
        else:
            frecuencia_palabra1[letra] = 1

    
    for letra in palabra2:
        if letra in frecuencia_palabra2:
            frecuencia_palabra2[letra] += 1
        else:
            frecuencia_palabra2[letra] = 1

       
    # Comparar las frecuencias de las letras
    return print(frecuencia_palabra1 == frecuencia_palabra2)

palabra1 = "hola como estas"
palabra2 = "ahol ocme osato"
son_anagramas(palabra1, palabra2)

