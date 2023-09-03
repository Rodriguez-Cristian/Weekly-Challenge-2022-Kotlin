#¿ES UN NÚMERO PRIMO?
 # Fecha publicación enunciado: 17/01/22
 # Fecha publicación resolución: 24/01/22
 # Dificultad: MEDIA
 
 # Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 # Hecho esto, imprime los números primos entre 1 y 100.

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    
    return True

numero = 1
for numero in range(100):
    if es_primo(numero):
        print(f"{numero} es un número primo.")
