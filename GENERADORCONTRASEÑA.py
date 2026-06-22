import random


def mostrar_menu(): #CREAMOS LA FUNCION PARA MOSTRAR EL MENU DEL PROGRAMA
    
    print("   GENERADOR DE CONTRASEÑAS SEGURO")
    print("1. Generar nueva contraseña")
    print("2. Salir")
    


def solicitar_longitud():  # Función para pedir la longitud de la contraseña
    longitud = 0

    while longitud < 8 or longitud > 10:
        longitud = int(input("Ingrese la longitud de la contraseña (8-10): "))

        if longitud < 8 or longitud > 10:
            print("Error: La longitud debe estar entre 8 y 10.")

    return longitud


def generar_contrasena(longitud):  # FUNCION PARA GENERAR LA CONTRASEÑA
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:,;#*"  #INGRESAMOS LOS CARACTERES LOS MISMO QUE SERVIRAN PARA CREAR LA CONTRASEÑA
    contrasena = ""

    for i in range(longitud):  #CREAMOS EL BUCLE PARA QUE ELIJA ALEATORIAMENTE LOS CARACTERES
        contrasena = contrasena + random.choice(caracteres) 

    return contrasena




