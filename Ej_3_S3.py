a4=0

while a4<1:
    print(" ")
    sbruto=float(input("Introduzca el salario bruto del empledo: C$ "))
    irenta = sbruto*0.1
    seguroSocial = sbruto*0.05
    fpensiones = sbruto*0.03
    descuentos = irenta+seguroSocial+fpensiones
    sneto = sbruto-descuentos
    print("El salario bruto es: C$ ", sbruto)
    print("El descuento total es: C$ ", descuentos)
    print("El salario neto es: C$ ", sneto)

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")