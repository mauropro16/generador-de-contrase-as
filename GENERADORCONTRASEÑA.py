import random


def mostrar_menu(): #CREAMOS LA FUNCION PARA MOSTRAR EL MENU DEL PROGRAMA
    
    print("   GENERADOR DE CONTRASEÑAS SEGURO")
    print("1. Generar nueva contraseña")
    print("2. Salir")
    


def solicitar_longitud():  # Función para pedir la longitud de la contraseña
    longitud = 0

    while longitud < 5 or longitud > 10:
        longitud = int(input("Ingrese la longitud de la contraseña (5-10): "))

        if longitud < 5 or longitud > 10:
            print("Error: La longitud debe estar entre 5 y 10.")

    return longitud


def generar_contrasena(longitud):  # FUNCION PARA GENERAR LA CONTRASEÑA
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:,;#*"  #INGRESAMOS LOS CARACTERES LOS MISMO QUE SERVIRAN PARA CREAR LA CONTRASEÑA
    contrasena = "" #CREAMOS LA VARIABLE VACIA PARA GUARDAR LA CONTRASEÑA

    for i in range(longitud):  #CREAMOS EL BUCLE PARA QUE ELIJA ALEATORIAMENTE LOS CARACTERES
        contrasena = contrasena + random.choice(caracteres) 
        
#------------------ PROGRAMA PRINCIPAL ------------------

opcion = 0  #CREAMOS LA VARIABLE OPCIÓN

#EL MENÚ SE REPETIRÁ HASTA QUE EL USUARIO ELIJA SALIR
while opcion != 2:

    mostrar_menu()  #LLAMAMOS A LA FUNCIÓN QUE MUESTRA EL MENÚ

    #SOLICITAMOS LA OPCIÓN AL USUARIO
    opcion = int(input("Seleccione una opción: "))

    #SI EL USUARIO ELIGE GENERAR UNA CONTRASEÑA
    if opcion == 1:

        longitud = solicitar_longitud()  #PEDIMOS LA LONGITUD

        contrasena = generar_contrasena(longitud)  #GENERAMOS LA CONTRASEÑA

        #MOSTRAMOS LA CONTRASEÑA GENERADA
        print("\nLa contraseña generada es:", contrasena)

    #SI EL USUARIO ELIGE SALIR
    elif opcion == 2:

        print("\nGracias por utilizar el Generador de Contraseñas.")

    #SI EL USUARIO INGRESA UNA OPCIÓN INCORRECTA
    else:

        print("\nError: Opción no válida. Intente nuevamente.")
    return contrasena




