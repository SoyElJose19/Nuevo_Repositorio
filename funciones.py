import csv
contactos=[]

def agregar_contacto():
    print ("\tAgregar contacto")
    nombre = validar_nombre()
    telefono = validar_telefono()
    correo= input("ingrese correo electronico: ")
    contacto={"nombre":nombre,
           "telefono":telefono,
           "correo":correo}
    contactos.append(contacto)
    print("CONTACTO AGREGADO")
def ver_lista():
    if not contactos:
        print("No existen contactos, agrege alguno")
    else:
        print("\tLISTA CONTACTOS")
        for con in contactos:
            print("NOMBRE: ", con["nombre"])
            print("TELEFONO: ", con["telefono"])
            print("CORREO: ", con["correo"])
            print()
def crear_csv():
    if not contactos:
        print("NO EXISTEN CONTACTOS!")
    else:
        nombre_archivo =input("Ingrese nombre para el archivo: ")+".csv"

        with open(nombre_archivo,"w",newline="") as file:
            escritor = csv.DictReader(file)
            escritor.writerows(contactos)
            print("ARCHIVO CREADO CON ÉXITO!")
            return
def salir():
    print("gracias, adios")
    exit()





#VALIDACIONES
def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 CARACTERES!")
def validar_telefono():
    while True:
        try:
            tel = int(input("Ingrese teléfono: "))
            if len(str(tel))==9 and str(tel)[0]=='9':
                return tel
            else:
                print("ERROR! EL TElÉFONO DEBE COMENZAR CON 9 Y TENER 9 DÍGITOS!")
        except:
            print("ERROR! INGRESE UN NÚMERO ENTERO!")