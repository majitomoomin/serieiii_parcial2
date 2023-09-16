#1. Elaborar una funcion que reciba 3 enteros y nos retome el valor promedio de los mismos

def promedio():
    entero1=int(input("Ingrese un número entero "))
    entero2=int(input("Ingrese el segundo número entero "))
    entero3=int(input("Ingrese el tercer número entero "))
    promedio=(entero1+entero2+entero3)/3
    print("El promedio de los 3 números enteros es: ", promedio)


#bloque principal del programa

promedio()
