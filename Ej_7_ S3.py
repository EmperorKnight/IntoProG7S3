#Ejercicio 7: Cálculo del precio final de un producto con impuestos y descuentos 

a4=0

while a4<1:
    print(" ")
    print("Introduzca la cantidad de productos a pagar: ")
    cantidad_producto = int(input("-> "))
    print("Introduzca el precio original de los producto: ")
    precio_original = float(input("-> "))

    a2 = precio_original
    a3 = 1

    while a3 < cantidad_producto:
        precio_original = float(input("-> "))
        a3 = a3 + 1
        a2 = a2 + precio_original

    print("Introduzca el porcentaje de descuento aplicado (solo el número, por favor): ")
    descuento = float(input("-> "))
    print("Introduzca el porcentaje de IVA (solo el número, por favor): ")
    IVA = float(input("-> "))

    precio_descuento = ((descuento / 100) * a2)
    precio_final = ((precio_descuento * IVA) / 100) + precio_descuento
    IVA2 = IVA / 100

    print(" ")
    print("Sumatoria de todos los producto: C$", a2)
    print("Descuento aplicado: ", descuento, "%")
    print("Resultado con descuento aplicado: C$", precio_descuento)
    print("IVA calculado: ", IVA2, "%")
    print("Total a pagar es: C$", precio_final)

    print(' ')
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
