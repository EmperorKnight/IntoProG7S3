a4=0

while a4<1:
    print(" ")
    base=float(input("Introduzca la base del rectángulo: "))
    altura=float(input("Introduzca la base del rectángulo: "))
    area = base * altura
    perimetro = (base*2)+(altura*2)
    print("El área del rectángulo es: ", area)
    print("El perimetro del rectángulo es: ", perimetro)

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")
