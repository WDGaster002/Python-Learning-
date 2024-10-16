##Creacion de calificacion de estudiantes

print("#################################")
print("# Calificaciones de estudiantes #")
print("#################################")

print("")

calificacion = float(input("Por favor ingresar su Nota Final: "))

if calificacion >= 90:
    print("")
    print("#################################")
    print("Felicidades, has aprobado con una calificacion sobresaliente")
    print("#################################")

elif calificacion >= 70:
    print("")
    print("#################################")
    print("Has aprobado satisfactoriamente")
    print("#################################")

elif calificacion >= 60:
    print("")
    print("#################################")
    print("Has aprobado, pero ncesitas mejorar un poco")
    print("#################################")

else:
    print("")
    print("#################################")
    print("Lo siento, has suspendido. Debes esforzarte mas en la prox. evaluacion")
    print("#################################")
    