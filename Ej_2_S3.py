#Ejercicio 2: Cálculo de área y perímetro de un rectángulo 

a4=0

while a4<1:
    print(" ")
    print("Introduzca la altura del rectángulo:")
    altura = float(input("-> "))
    print("Introduzca la base del rectángulo:")
    base = float(input("-> "))
   
    area = base * altura
    perimetro = (base * 2) + (altura * 2)
    
    print(" ")
    print(f"El área del rectángulo es: {area:.2f}")
    print(f"El perimetro del rectángulo es: {perimetro:.2f}")

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")
