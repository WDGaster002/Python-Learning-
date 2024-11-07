import os
os.system("cls")

tupla = ("manzana", "uva", "fresa", "melon",  "naranja", "caja", "mesa", "circulo", "cuadrado", "rectangulo", "esfera")


print("")
print("##########################")
print("#  Buscador de Palabras  #")
print("##########################")
print("")

print("############################################")
buscar = input("Favor escribir una  palabra a buscar: ")
print("############################################")

if buscar in tupla:
    print("")
    print("La palabra ","'", buscar,"'" ," está en la tupla")
    print("")
    

else:
    print("")
    print("La palabra que buscas no está en la tupla")
    print("")
    