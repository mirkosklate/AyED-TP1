import sys
import getpass


usuarioAdmin = "admin"
contrasenaAdmin = "admin"
tipoUsuario = "Administrador"

def cartel_desarrollo():
    print("Seccion en desarrollo, intente mas tarde.\n")

def inicio_sesion():
    intentos = 3

    while(intentos > 0):
        print("\nBienvenido. Para iniciar sesion, por favor introduzca sus datos a continuacion.\n") 
        usuario = input("Usuario: ")    
        contrasena = getpass.getpass("Contraseña: ")

        if usuario == usuarioAdmin:
            if contrasena == contrasenaAdmin:
                print(f"Usuario validado exitosamente. Bienvenido {tipoUsuario}\n")
                menu_principal()
            else:
                print("Contraseña incorrecta. Intente nuevamente")
        else:
            print("Usuario incorrecto. Intente nuevamente.")
        
        intentos -= 1
        print(f"\n{intentos} intentos de inicio de sesion restantes.\n")

    if intentos == 0:
        print("\nDemasiados intentos de inicio de sesion incorrectos. Terminando programa.")
        exit() #no se puede usar esto, sacarlo xd lol porfa


def menu_principal():
    opcion = 1
    while(opcion != 0):
        print(f"Menu del {tipoUsuario}\n")
        print("1. Gestion de aerolineas")
        print("2. Aprobar/Denegar promociones")
        print("3. Gestion de novedades")
        print("4. Reportes")
        print("5. Terminar sesion")

        opcion = int(input("Seleccion de opcion: "))
        while(opcion < 1 or opcion > 5):
            opcion = int(input("Opcion invalida, intente nuevamente: "))
        match opcion:
            case 1: menu_GestionAerolineas()
            case 2: cartel_desarrollo()
            case 3: menu_GestionNovedades()
            case 4: menu_Reportes()
            case 5: inicio_sesion()

def menu_GestionAerolineas():
    opcion2 = 1
    while(opcion2 != 0):
        print("1. Crear Aerolinea")
        print("2. Modificar Aerolinea")
        print("3. Eliminar Aerolinea")
        print("4. Volver")

        opcion2 = int(input("Seleccion de opcion: "))
        while(opcion2 < 1 or opcion2 > 4):
            opcion2 = int(input("Opcion invalida, intente nuevamente: "))
        match opcion2:
            case 1: gestionAerolineas_Crear()
            case 2: cartel_desarrollo()
            case 3: cartel_desarrollo()
            case 4: menu_principal()

def menu_GestionNovedades():
    opcion3 = 1
    while(opcion3 != 0):
        print("1. Crear Novedad")
        print("2. Modificar Novedad")
        print("3. Eliminar Novedad")
        print("4. Ver Novedades")
        print("5. Volver")

        opcion3 = int(input("Seleccion de opcion: "))
        while(opcion3 < 1 or opcion3 > 5):
            opcion3 = int(input("Opcion invalida, intente nuevamente: "))
        match opcion3:
            case 1: cartel_desarrollo()
            case 2: cartel_desarrollo()
            case 3: cartel_desarrollo()
            case 4: cartel_desarrollo()
            case 5: menu_principal() 

def menu_Reportes():
    opcion4 = 1
    while(opcion4 != 0):
        print("1. Reporte de Ventas")
        print("2. Reporte de Vuelos")
        print("3. Reporte de Usuarios")
        print("4. Volver")

        opcion4 = int(input("Seleccion de opcion: "))
        while(opcion4 < 1 or opcion4 > 4):
            opcion4 = int(input("Opcion invalida, intente nuevamente: "))
        match opcion4:
            case 1: cartel_desarrollo()
            case 2: cartel_desarrollo()
            case 3: cartel_desarrollo()
            case 4: menu_principal() 

def gestionAerolineas_Crear():
    exit()

inicio_sesion()
