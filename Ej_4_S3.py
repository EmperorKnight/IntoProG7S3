a4=0

while a4<1:
    print(" ")
    pTramo = int(input("Introduzca el tiempo del primer tramo del vuelo: "))
    pEscala = int(input("Introduzca el tiempo de la primera escala: "))
    sTramo = int(input("Introduzca el tiempo del segundo tramo del vuelo: "))
    sEscala = int(input("Introduzca el tiempo de la segunda escala: "))
    tTramo = int(input("Introduzca el tiempo del tercer tramo del vuelo: "))
	
    tiempo_viaje = ((((pTramo+pEscala)+sTramo)+sEscala)+tTramo)
	
    print("El tiempo total del vuelo es: ", tiempo_viaje)
    
    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")