from os import system
from funciones import *

paciente = []
while True:
    print("1.- agregar paciente")
    print("2.- buscar paciente por nombre")
    print("3.- atender paciente")
    print("4.- calcular imc")
    print("5.- cerrar sistema")
    opc = validar_entero(1,5,"opcion")
    match(opc):
        case 1:
            agregar_paciente(paciente)
        case 2:
            buscar_paciente(paciente)
        case 3:
            atender_paciente(paciente)
        case 4:
            calcular_imc(paciente)
        case 5:
            print("cerrando sistema")
            break