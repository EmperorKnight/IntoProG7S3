#Ejercicio 1: Conversión de temperatura 

a4=0

while a4<1:
    print(" ")
    print("Grados fahrenheit:") #float = real
    grado_f = float(input("-> "))

    grado_c = ((grado_f - 32) * 5) / 9
    grado_k = 273.15 + grado_c
    
    print(f"°C {grado_c:.2f}")
    print(f"°K {grado_k:.2f}")

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")