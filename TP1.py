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
        contrasena = input("Contraseña: ")

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
        exit()

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
            case 3: cartel_desarrollo()
            case 4: cartel_desarrollo()
            case 5: inicio_sesion()

def menu_GestionAerolineas():
    opcion2 = 1
    while (opcion2 != 0):
        print("1. Crear Aerolinea")
        print("2. Modificar Aerolinea")
        print("3. Eliminar Aerolinea")
        print("4. Volver")

        opcion2 = int(input("Seleccion de opcion: "))
        while(opcion2 < 1 or opcion2 > 4):
            opcion2 = int(input("Opcion invalida, intente nuevamente: "))
        match opcion2:
            case 1: cartel_desarrollo()
            case 2: cartel_desarrollo()
            case 3: cartel_desarrollo()
            case 4: menu_principal()

inicio_sesion()
