#Ejercicio 3: Cálculo del salario neto de un empleado 

a4=0

while a4<1:
    print(" ")
    print("Introduzca el salario bruto del empledo:")
    salario_bruto = float(input("-> "))
    
    impuesto_renta = salario_bruto * 0.1
    seguro_social = salario_bruto * 0.05
    fondo_pensiones = salario_bruto * 0.03
    descuentos = impuesto_renta + seguro_social + fondo_pensiones
    salario_neto = salario_bruto - descuentos    

    print(" ")
    print("El salario bruto es: C$ ", salario_bruto)
    print("El descuento total es: C$ ", descuentos)
    print("El salario neto es: C$ ", salario_neto)

    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")