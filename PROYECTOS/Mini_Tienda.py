##BIENVENIDO AL SEGUNDO PROGRAMA QUE CREO XD

import os
## os.system("cls")

verdura_total = 0
fruta_total = 0

def Menu_Principal():
    os.system("cls")
    print("#############################################")
    print("#     BIENVENIDO A MINI TIENDA VIRTUAL      #")
    print("#         CREADO POR: WD Gaster002          #")
    print("#############################################")
    print("#                                           #")
    print("#    1. COMPRAR VEGETALES                   #")
    print("#    2. COMPRAR FRUTAS                      #")
    print("#    3. VER TOTAL                           #")
    print("#    4. SALIR                               #")
    print("#############################################")
    print("")


##################VERDURAS###########################

def opc1():
    os.system("cls")
    print("###############################################")
    print("#            SECCION DE VEGETALES             #")
    print("###############################################")
    print("#    PRODUCTO                    #   PRECIO   #")
    print("###############################################")
    print("#                                #            #")
    print("#    1. TOMATE                   # $1.23 x Lb #")
    print("#    2. LECHUGA                  # $2.30 x Lb #")
    print("#    3. PEPINO                   # $2.55 x Lb #")
    print("#                                #            #")
    print("###############################################")
    print("")

##VERDURAS SELECCION

def ver1():
    global verdura_total
    print("")
    print("###############################################")
    tomate = int(input("favor seleccionar cuantas libras de tomate llevara: "))
    if  tomate == 0:
        
        print("###############################################")
        lechuga = int(input("favor seleccionar cuantas libras de lechuga llevara: "))
        if  lechuga == 0:
            
            print("###############################################")
            pepino = int(input("favor seleccionar cuantas libras de pepino llevara: "))
            if pepino == 0:
                print("")
                print("no selecciono ningun producto")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  pepino > 0:
                print("")
                print("###############################################")
                print("selecciono ",  pepino, " libras de pepino")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()

        if   lechuga > 0:
            print("")
            print("###############################################")
            print("selecciono ",  lechuga, " libras de lechuga")
            
            pepino = int(input("favor seleccionar cuantas libras de pepino llevara: "))
            if pepino == 0:
                print("")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  pepino > 0:
                print("")
                print("###############################################")
                print("selecciono ",  pepino, " libras de pepino")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()
    
    if tomate > 0:
        print("###############################################")
        print("Selecciono ", tomate, " libras de tomate")
        
        print("###############################################")
        lechuga = int(input("favor seleccionar cuantas libras de lechuga llevara: "))
        if  lechuga == 0:
           
            print("###############################################")
            pepino = int(input("favor seleccionar cuantas libras de pepino llevara: "))
            if pepino == 0:
                print("")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  pepino > 0:
                print("")
                print("###############################################")
                print("selecciono ",  pepino, " libras de pepino")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()

        if   lechuga > 0:
            print("###############################################")
            print("selecciono ",  lechuga, " libras de lechuga")
            
            print("###############################################")
            pepino = int(input("favor seleccionar cuantas libras de pepino llevara: "))
            if pepino == 0:
                print("")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  pepino > 0:
                print("")
                print("###############################################")
                print("selecciono ",  pepino, " libras de pepino")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()

    #PRECIOS VERDURAS

    t1 = 1.23
    l1 = 2.30
    p1 = 2.55

    #PROCESOS

    tomate_total =  tomate * t1
    lechuga_total = lechuga * l1
    pepino_total = pepino * p1

    verdura_total = tomate_total + lechuga_total + pepino_total



#######################FRUTAS##############################

def opc2():
    os.system("cls")
    print("###############################################")
    print("#            SECCION DE FRUTAS                #")
    print("###############################################")
    print("#    PRODUCTO                    #   PRECIO   #")
    print("###############################################")
    print("#                                #            #")
    print("#    1. MANZANA                  # $1.56 x Lb #")
    print("#    2. UVAS                     # $1.00 x Lb #")
    print("#    3. NARANJA                  # $2.00 x Lb #")
    print("#                                #            #")
    print("###############################################")
    print("")

def frut1():
    global fruta_total
    print("")
    print("###############################################")
    manzana = int(input("favor seleccionar cuantas libras de manzana llevara: "))
    if  manzana == 0:
        
        print("###############################################")
        uvas = int(input("favor seleccionar cuantas libras de uvas llevara: "))
        if  uvas == 0:
            
            print("###############################################")
            naranja = int(input("favor seleccionar cuantas libras de naranja llevara: "))
            if naranja == 0:
                print("")
                print("no selecciono ningun producto")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  naranja > 0:
                print("")
                print("###############################################")
                print("selecciono ",  naranja, " libras de naranjas")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()

        if   uvas > 0:
            print("")
            print("###############################################")
            print("selecciono ",  uvas, " libras de uvas")
            
            print("###############################################")
            naranja = int(input("favor seleccionar cuantas libras de naranjas llevara: "))
            if naranja == 0:
                print("")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  naranja > 0:
                print("")
                print("###############################################")
                print("selecciono ",  naranja, " libras de naranjas")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()
    
    if manzana > 0:
        print("###############################################")
        print("Selecciono ", manzana, " libras de manzanas")
        
        print("###############################################")
        uvas = int(input("favor seleccionar cuantas libras de uvas llevara: "))
        if  uvas == 0:
           
            print("###############################################")
            naranja = int(input("favor seleccionar cuantas libras de naranjas llevara: "))
            if naranja == 0:
                print("")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  naranja > 0:
                print("")
                print("###############################################")
                print("selecciono ",  naranja, " libras de naranjas")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()

        if   uvas > 0:
            print("###############################################")
            print("selecciono ",  uvas, " libras de uvas")
            
            print("###############################################")
            naranja = int(input("favor seleccionar cuantas libras de naranjas llevara: "))
            if naranja == 0:
                print("")
                input("Presione Enter para continuar...")
                Menu_Principal()
            
            if  naranja > 0:
                print("")
                print("###############################################")
                print("selecciono ",  naranja, " libras de naranjas")
                print("")
                input("Precione Enter para continuar...")
                Menu_Principal()

    #PRECIOS FRUTAS

    m1 = 1.56
    u1 = 1.00
    n1 = 2.00

    #PROCESOS

    manzana_total = manzana *  m1
    uvas_total = uvas * u1
    naranja_total = naranja * n1

    fruta_total =  manzana_total + uvas_total + naranja_total



####################TOTAL############################

def opc3():

    global verdura_total
    global fruta_total

    total = verdura_total + fruta_total

    os.system("cls")
    print("##############################################")
    print("#            SECCION DE TOTAL                #")
    print("##############################################")
    print("#    PRODUCTOS                   #   PRECIO  #")
    print("##############################################")
    print("#                                #           ")
    print("#    VERDURAS                    # $",round(verdura_total, 2))
    print("#    FRUTAS                      # $",round(fruta_total, 2))
    print("#                                #           ")
    print("##############################################")
    print("#    TOTAL                       # $",round(total, 2), "  #")
    print("##############################################")
    print("")
    input("Seleccione una Enter para continuar...")
    Menu_Principal()


def opc4():
    os.system("cls")
    print("##############################################")
    print("#            SECCION DE SALIR                #")
    print("##############################################")
    print("#    GRACIAS POR SU VISITA                   #")
    print("##############################################")
    print("")
    input("Presione Enter para continuar...")
    os.system("cls")
    exit()






while  True:
    Menu_Principal()
    opc = input("Ingrese la opcion que desee: ")
    if opc == "1":
        opc1()
        ver1()
    
    if opc == "2":
        opc2()
        frut1()

    if  opc == "3":
        opc3()
    
    if  opc == "4":
        opc4()
