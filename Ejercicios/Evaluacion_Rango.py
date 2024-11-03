print("")
print("################################")
print("#     Verificador de Rango     #")
print("################################")
print("")


num =  int(input("Ingrese un valor entero: "))

match num:
    case num if num < 0:
        print("")
        print("##########################################")
        print("# El número ", num, " esta en el rango 1 #")
        print("#       Rango 1: Numeros Negativos       #")
        print("##########################################")
        print("")

    case num if num >= 0 & num < 10:

        print("")
        print("#########################################")
        print("# El número ", num, " esta entre 0 y 10 #",)
        print("#     Rango 2: Numero entre 0 y 10      #")
        print("#########################################")
        print("")

    case num if num >= 10:
        print("")
        print("#############################################")
        print("# El número ", num, " es mayor o igual a 10 #")
        print("# Rango 3: Numeros Mayores o igual a 10     #")
        print("#############################################")
        print("")


