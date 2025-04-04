#Ejercicio 5: Conversión de unidades de tiempo

a4=0

while a4<1:
    print(" ")
    print('Introduzca la cantidad total de segundos:')
    total_segundos = int(input("-> "))

    horas = int(total_segundos/3600)
    minutos = int((total_segundos-(horas*3600))/60)
    segundos = int(total_segundos-(minutos*60))

    print(" ")
    print('Conversion completa: ', horas, ':', minutos, ':', segundos)
    
    print (" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")