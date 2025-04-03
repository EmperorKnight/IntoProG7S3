import math
a4=0

while a4<1:
    print(" ")
    print("Introduzca el radio del cilindro: ")
    radio = float(input("-> "))
    print("Introduzca la altura del cilindro: ")
    altura = float(input("-> "))

    area_base = math.pi * (radio ** 2)
    volumen_cilindro = area_base * altura 
    area_lateral = (((2 * math.pi) * radio) * altura)
    area_total = area_lateral + (2 * area_base)
    area_superficial = area_total

    print("La altura ingresada es de:", altura)
    print("El radio ingresada es de:", radio)   
    print("El volumen del cilindro es de:", volumen_cilindro)
    print("El area superficial del cilindro es de:", area_superficial)

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())