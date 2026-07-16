from os import system
system("cls")

def validar_nombre():
    while True:
        nombre = input("ingrese nombre: ")
        if nombre == "" or " " in nombre:
            print("error, nombre incorrecto")
        else:
            return nombre
def validar_entero(min,max,texto):
    while True:
        try:
            numero = int(input(f"ingrese {texto} : "))
            if min <= numero <= max:
                return numero
            else:
                print(f"el rango permitido es: {min} {max}")
        except:
            print("error, no se permite ingresar letras")
def validar_decimal(min,max,texto):
    while True:
        try:
            numero = float(input(f"ingrese {texto} : "))
            if min <= numero <= max:
                return numero
            else:
                print(f"el rango permitido es: {min} {max}")
        except:
            print("error, no se permite ingresar letras")
def validar_seguro():
    print("tiene seguro?")
    print("1.- si")
    print("2.- no")
    opc = validar_entero(1,2,"opcion")
    if opc == 1:
        return True
    else:
        return False
def agregar_paciente(lista_paciente):
    paciente={
        "nombre" : validar_nombre(),
        "edad" : validar_entero(0,140,"edad"),
        "peso" : validar_decimal(3,200,"peso"),
        "estatura" : validar_decimal(0.3,3.0,"estatura"),
        "seguro" : validar_seguro()
    }
    lista_paciente.append(paciente)
def buscar_paciente(lista_paciente):
    nombre = validar_nombre()
    for paciente in lista_paciente:
        if paciente["paciente"] == nombre:
            print(f"paciente nombre : {paciente['nombre']}")
            print(f"paciente edad : {paciente['edad']}")
            print(f"paciente peso : {paciente['peso']}")
            print(f"paciente estatura : {paciente['estatura']}")
            if paciente["seguro"]:
                print("paciente tiene seguro")
            else:
                print("paciente no tiene seguro")
def atender_paciente(lista_paciente):
    nombre = validar_nombre()
    for paciente in lista_paciente:
        if paciente["nombre"] == nombre:
            lista_paciente.remove(paciente)
            break
def calcular_imc(lista_paciente):
    for paciente in lista_paciente:
        paciente["imc"] = paciente["peso"]/(paciente["estatura"]**2)