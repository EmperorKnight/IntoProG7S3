a4=0

while a4<1:
    print(" ")
    altura=float(input('Introduzca la altura en metros: '))
    peso=float(input("Introduzca el peso en kilogramos: "))

    IMC = peso/(altura * altura)

    if IMC<=18.5:
        print("Composición corporal:")
        print("Peso inferior al normal")
        print("El peso ingresado es:", peso, "kg")
        print("La altura ingresada es:", altura, "m")
        print("El indice de masa corporal es:", IMC)
    elif IMC>=18.6 and IMC <= 24.9:
        print("Composición corporal:")
        print("Normal")
        print("El peso ingresado es:", peso, "kg")
        print("La altura ingresada es:", altura, "m")
        print("El indice de masa corporal es:", IMC)
    elif IMC>=25.0 and IMC <= 29.9:
        print("Composición corporal:")
        print("Peso superior al normal")
        print("El peso ingresado es:", peso, "kg")
        print("La altura ingresada es:", altura, "m")
        print("El indice de masa corporal es:", IMC)
    elif IMC >=30.0:
        print("Composición corporal:")
        print("Obesidad")
        print("El peso ingresado es:", peso, "kg")
        print("La altura ingresada es:", altura, "m")
        print("El indice de masa corporal es:", IMC)
        
    print(' ')
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
