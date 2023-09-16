#2 Confeccionar  una funcion que calcule la superficie de un rectangulo y la retorne, la funcion recibe como parametros los valores
#de dos de sus lados; en el bloque principal del programa cargar los lados de dos rectangulos y luego mostrar cual de los dos tiene una superficie mayor.

def rectangulo_superficie(v1, v2):
    ancho=[]
    largo=[]
    superficie=ancho*largo
    return(superficie)

def lados(v1, v2):
    if v1>v2:
        print("Es mayor ", v1)
    else:
        if v2>v1:
            print("Es mayor ", v2)

def valores():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    mostrar_mayor(valor1,valor2)

#Bloque principal

valores()
