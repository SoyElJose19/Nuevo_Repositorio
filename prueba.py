import time, os
from funciones import *

while True:
    os.system("cls")
    print("1.- Agregar contacto")
    print("2.- Ver Lista Contactos")
    print("3.- Crear archivo CSV")
    print("4.- Salir")
    opc=int(input("Ingrese una opción: "))
    os.system("cls")
    if opc ==1:
        agregar_contacto()
    elif opc ==2:
        ver_lista()
    elif opc ==3:
        crear_csv()
    else:
        salir()
    time.sleep(3)