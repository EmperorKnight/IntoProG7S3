print(" ")
total_segundos = int(input('Introduzca la cantidad total de segundos: '))

horas = int(total_segundos/3600)
minutos = int((total_segundos-(horas*3600))/60)
segundos = int(total_segundos-(minutos*60))

print(" ")
print('Conversion completa: ', horas, ':', minutos, ':', segundos)
print (" ")