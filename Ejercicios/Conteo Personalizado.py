import os
os.system("cls")

contador = 1

print("")
print("##############################")
print("#   Contador Personalizado   #")
print("##############################")
print("")


num = int(input("Favor ingresar un numero: "))

print("")
while num > 0:
    print(contador)
    contador += 1

    if  contador > int(num):
        print("")
        print("Conteo Completado")
        print("")
        break