import funciones

opcion=0
archivo="archivo2.txt"
funciones.claves()
clavePrivada=funciones.cargarClavePrivada()
clavePublica=funciones.cargarClavePublica()



while opcion !=5:
    print("\nSeleccione una opción\n")
    print("1.-Leer Archivo\n2.-Agregar texto al archivo\n3.-Encriptar\n4.-Desencriptar\n5.-Salir")
    opcion=int(input("Ingresa una opción: "))

    if opcion==1:
        print("El contenido del archivo es: ")
        funciones.leerArchivo(archivo)
    elif opcion==2:
        linea=input("Introduce el texto que desea agregar al archivo: ")
        funciones.escribirArchivo(linea,archivo)
    elif opcion==3:
        print("Encriptando archivo...")
        funciones.cifrado(archivo,clavePublica)
        print("Archivo encriptado")
    elif opcion==4:
        print("Desencriptando archivo...")
        funciones.descifrado(archivo,clavePrivada)
        print("Archivo desencriptado")
    elif opcion==5:
        exit()
    else:
        print("\nOpción incorrecta")