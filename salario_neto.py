sbruto=float(input("Introduzca el salario bruto del empledo: C$ "))
irenta = sbruto*0.1
seguroSocial = sbruto*0.05
fpensiones = sbruto*0.03
sneto = sbruto - (irenta+seguroSocial+fpensiones)
print("El salario bruto es: C$ ", sbruto)
print("El resultado despues de aplicar el impuesto sobre la renta: C$ ", irenta)
print("El resultado despues de aplicar el seguro social: C$ ", seguroSocial)
print("El resultado despues de aplicar el fondo de pensiones: C$ ", fpensiones)
print("El salario neto es: C$ ", sneto)