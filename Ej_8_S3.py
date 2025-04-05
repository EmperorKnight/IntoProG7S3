# Ejercicio 8: Conversión de una cantidad en dólares a distintas monedas

euro = 0.91
libra_santa_helena = 0.77
libra_egipcia = 50.59
libra_esterlina = 0.76
libra_sudanesa = 600.50
libra_libanesa = 89275.07
yen_japones = 145.47

a4=0

while a4<1:
    print(" ")
    print("Introduzca la cantidad de dólares a convertir: ")
    dolares = float(input("-> "))

    cantidad_euros=dolares*euro
    cantidad_libra1 = dolares * libra_santa_helena
    cantidad_libra2 = dolares * libra_egipcia
    cantidad_libra3 = dolares * libra_esterlina
    cantidad_libra4 = dolares * libra_sudanesa
    cantidad_libra5 = dolares * libra_libanesa
    cantidad_yenes = dolares * yen_japones

    print("La cantidad de dolares a euros es: ", cantidad_euros)
    print("La cantidad de dolares a Libra de Santa Helena es: ", cantidad_libra1)
    print("La cantidad de dolares a Libra Egipcia es: ", cantidad_libra2)
    print("La cantidad de dolares a Libra Estarlina es: ", cantidad_libra3)
    print("La cantidad de dolares a Libra Sudanesa es: ", cantidad_libra4)
    print("La cantidad de dolares a Libra libanesa es: ", cantidad_libra5)
    print("La cantidad de dolares al Yen Japones es: ", cantidad_yenes)

    print(' ')
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())