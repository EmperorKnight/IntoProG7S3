peso=float(input('Introduzca el peso en kilogramos: '))
altura=float(input("Introduzca la altura en metros: "))

IMC = peso/(altura ** 2)
IMC = (IMC * 100) / 100

print("El peso ingresado es:", peso, "kg")
print("La altura ingresada es:", altura, "m")
print("El indice de masa corporal es:", IMC)
