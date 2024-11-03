##BIENVENIDO PIBE, EN ESTE .PY ESTOY IMPLEMENTANDO PRACTICAMENTE TODO LO APRENDIDO XD

##ESTO DE AQUI SI ME PUSE A INVESTIGAR PARA LIMPIAR LA TERMINAL JAJA
import os



##creacion de clases

def menu_Principal():
    os.system("cls")
    print("###############################")
    print("#         Calculadora         #")
    print("#   Creado por: WD Gaster002  #")
    print("###############################")
    print("")
    print("###################################")
    print("# ¿Qué operación deseas realizar? #")
    print("#                                 #")
    print("#   1. Suma                       #")
    print("#   2. Resta                      #")
    print("#   3. Multiplicación             #")
    print("#   4. División                   #")
    print("#   5. Salir                      #")
    print("###################################")
    print("")
    


#############SUMA#####################

def suma_Completa():
    print("")
    print("########################################")
    print("#  Has seleccionado la opción 1: Suma  #")
    print("########################################")
    print("")

    print("#####################################")
    sum1 = float(input("favor escribir el primer valor: "))
    print("#####################################")
    sum2 = float(input("favor escribir el segundo valor: "))
    print("#####################################")

    ##PROCESO
    sum3 = sum1 + sum2
    print("")
    print("####################")
    print(" Resultado: ", sum3 )
    print("####################")
    print("")
    input("Precione una tecla para continuar...")
    os.system("cls")


##################RESTA#######################

def resta_Completa():
    print("")
    print("########################################")
    print("#  Has seleccionado la opción 2: Resta #")
    print("########################################")
    print("")
    print("#####################################")
    rest1 = float(input("favor escribir el primer valor: "))
    print("#####################################")
    rest2 = float(input("favor escribir el segundo valor: "))
    print("#####################################")
    
    ##PROCESO
    rest3 = rest1 - rest2
    print("")
    print("####################")
    print(" Resultado: ", rest3 )
    print("####################")
    print("")
    input("Precione una tecla para continuar...")
    os.system("cls")


###################MULTIPLICACION###################

def multiplicacion_Completa():
    print("")
    print("################################################")
    print("# Has seleccionado la opción 3: Multiplicación #")
    print("################################################")
    print("")
    print("#####################################")
    multi1 = float(input("favor escribir el primer valor: "))
    print("#####################################")
    multi2 = float(input("favor escribir el segundo valor: "))
    print("#####################################")

    ##PROCESO
    multi3 =  multi1 * multi2
    print("")
    print("####################")
    print("# Resultado: ", multi3)
    print("####################")
    print("")
    input("Precione una tecla para continuar...")
    os.system("cls")

###################DIVISION##########################

def division_Completa():
    print("")
    print("##########################################")
    print("# Has seleccionado la opción 4: División #")
    print("##########################################")
    print("")
    print("#####################################")
    divi1 = float(input("favor escribir el primer valor: "))
    print("#####################################")
    divi2 = float(input("favor escribir el segundo valor: "))
    print("#####################################")

    ##CONDICION
    if  divi2 == 0:
        print("")
        print("##################################")
        print("# No se puede dividir entre cero #")
        print("##################################")
        print("")
        input("Precione una tecla para continuar...")
        os.system("cls")
        menu_Principal()


    else:
        ##PROCESO
        divi3 =  divi1 / divi2

        print("")
        print("##########################")
        print("# Resultado: ", divi3)
        print("##########################")
        print("")
        input("Precione una tecla para continuar...")
        os.system("cls")


##############Salir################
def salir():
    print("")
    print("#######################################")
    print("# Has seleccionado la opción 5: Salir #")
    print("#######################################")
    print("")
    print("Gracias por utilizar el programa")
    input("Precione una tecla para continuar...")
    os.system("cls")
    exit()


##USO DE WHILE

while True:
    menu_Principal()
    opcion = int(input("Escriba el número de la opcion: "))
    os.system("cls")

    if opcion == 1:
        suma_Completa()

    if opcion == 2:
        resta_Completa()
    
    if opcion == 3:
        multiplicacion_Completa()
    
    if opcion == 4:
        division_Completa()
    
    if  opcion == 5:
        salir()

    else:
        input("Opcion Incorrecta, intentelo de nuevo...")