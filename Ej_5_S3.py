#Ejercicio 5: Conversión de unidades de tiempo

a4=0

while a4<1:
    print(" ")
    print('Introduzca la cantidad total de segundos:')
    total_segundos = int(input("-> "))

    horas = total_segundos // 3600
    segundos_restantes = total_segundos - (horas * 3600)
    minutos = segundos_restantes // 60
    segundos = segundos_restantes - (minutos * 60)

    print(" ")
    print('Conversion completa: ')
    print("Horas: ", horas)
    print("Minutos: ", minutos)
    print("Segundos: ", segundos)
    
    print (" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")