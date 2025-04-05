#Ejercicio 4: Cálculo del tiempo total de un viaje con escalas 

a4=0

while a4<1:
    print(" ")
    
    print("Introduzca el tiempo del primer tramo del vuelo (en horas):")
    primer_tramo = int(input("-> "))
    print("Introduzca el tiempo de la primera escala (en horas):")
    primera_escala = int(input("-> "))
    print("Introduzca el tiempo del segundo tramo del vuelo (en horas):")
    segundo_tramo = int(input("-> "))
    print("Introduzca el tiempo de la segunda escala (en horas):")
    segunda_escala = int(input("-> "))
    print("Introduzca el tiempo del tercer tramo del vuelo (en horas):")
    tercer_tramo = int(input("-> "))
	
    tiempo_viaje = ((((primer_tramo + primera_escala) + segundo_tramo) + segunda_escala) + tercer_tramo)
	
    print("El tiempo total del vuelo es: ", tiempo_viaje)
    
    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO >= 1")
    a4 = int(input())
    print(" ")