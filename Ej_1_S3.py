a4=0

while a4<1:
    print(" ")
    grado_f = float(input("Grados fahrenheit: ")) #float = real
    grado_c = ((grado_f - 32)*5)/9
    print("C",grado_c)
    
    print(" ")
    print("¿Desea reintroducir los valores?")
    print("SI = 0 | NO = 1")
    a4 = int(input())
    print(" ")