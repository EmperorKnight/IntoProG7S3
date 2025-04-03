a4=0

while a4<1:
    print(" ")
    print("Introduzca el tiempo de la pelicula en minutos: ")   
    tiempo_pelicula=int(input("-> "))
    print("Introduzca la duración de los comerciales previos: ")
    tiempo_comer_prev=int(input("-> "))
    print("Introduzca la cantidad de pausas comerciales durante la pelicula: ")
    cantidad_comer_pausas=int(input("-> "))
    print("Introduzca la duración de cada pausa comercial: ")
    tiempo_comer_pausas=int(input("-> "))

    a3=1
    a2=tiempo_comer_pausas

    while a3<cantidad_comer_pausas:
        tiempo_comer_pausas=int(input("-> "))
        a2=a2+tiempo_comer_pausas
        a3=a3+1

    total_comerciales=a2*cantidad_comer_pausas
    duracion_total=(tiempo_pelicula+tiempo_comer_prev)+total_comerciales

    print("La duración original de la pelicula es de:", tiempo_pelicula)
    print("La duración de los comerciales es de:", total_comerciales)
    print("El tiempo total de la proyección es de:", tiempo_pelicula,"minutos con", duracion_total,"segundos")

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())