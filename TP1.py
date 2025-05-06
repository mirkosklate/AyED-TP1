import os
import time
import pwinput

#Ponele que se puede usar variables globales
usuarioAdmin = "admin"
contrasenaAdmin = "admin"
tipoUsuario = "Administrador"

#Novedades
codigoNovedad1 = "Nov001"
textoNovedad1 = "Nuevos horarios de salidas de vuelos:\n Se han actualizado los horarios de salidas de vuelos" \
" para poder llevar a cabo de manera mas eficiente las operaciones en las instalaciones.\n"
fechaPublicacionNovedad1 = "21-04-25"
fechaExpiracionNovedad1 = "28-04-25"

codigoNovedad2 = "Nov002"
textoNovedad2 = "Relocalizacion del area de mantenimiento:\n Se ha relocalizado al subsuelo 1 el deposito de insumos de mantenimiento y limpieza de las intalaciones, " \
"recuerde retirar la nueva tarjeta de acceso en las oficinas de administracion.\n"
fechaPublicacionNovedad2 = "24-04-25"
fechaExpiracionNovedad2 = "01-05-25"

codigoNovedad3 = "Nov003"
textoNovedad3 = "Recordatorio:\n A raiz del incidente del dia de ayer, " \
"se solicita encarecidamente asegurar correctamente las señalizaciones correspondientes a la presencia de fosas en los lugares en mantenimiento.\n"
fechaPublicacionNovedad3 = "28-05-25"
fechaExpiracionNovedad3 = "05-05-25"

contadorArg = 0
contadorBra = 0
contadorChi = 0

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def cartel_desarrollo():
    print("\nSeccion en desarrollo, intente mas tarde.\n")
    time.sleep(3)
    limpiar_pantalla()

def inicio_sesion(contadorArg, contadorBra, contadorChi, 
                  codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                  codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                  codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3):
    limpiar_pantalla()

    intentos = 3

    while(intentos > 0):
        print("\nBienvenido. Para iniciar sesion, por favor introduzca sus datos a continuacion.\n") 
        usuario = input("Usuario: ")    
        contrasena = pwinput.pwinput("Ingrese su contraseña... ")

        if usuario == usuarioAdmin:
            if contrasena == contrasenaAdmin:
                print(f"Usuario validado exitosamente. Bienvenido {tipoUsuario}\n")
                menu_principal(contadorArg, contadorBra, contadorChi, 
                               codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                               codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                               codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)
            else:
                print("Contraseña incorrecta. Intente nuevamente")
        else:
            print("Usuario incorrecto. Intente nuevamente.")
        
        intentos -= 1
        print(f"\n{intentos} intentos de inicio de sesion restantes.\n")

    if intentos == 0:
        print("\nDemasiados intentos de inicio de sesion incorrectos. Terminando programa.")
        time.sleep(3)

def menu_principal(contadorArg, contadorBra, contadorChi, codigoNovedad1, 
                   textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                   codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                   codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3):
    limpiar_pantalla()

    opcion = 1
    while(opcion != 0):
        print(f"Menu del {tipoUsuario}\n")
        print("1. Gestion de aerolineas")
        print("2. Aprobar/Denegar promociones")
        print("3. Gestion de novedades")
        print("4. Reportes")
        print("5. Terminar sesion")

        opcion = int(input("Seleccion de opcion: ")) 
        while(opcion < 1 or opcion > 5 or opcion):
            opcion = int(input("Opcion invalida, intente nuevamente: "))
        match opcion:
            case 1: 
                menu_GestionAerolineas(contadorArg, contadorBra, contadorChi)
            case 2: 
                cartel_desarrollo()
            case 3: 
                menu_GestionNovedades(codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                                      codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                                      codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)
            case 4: 
                menu_Reportes()
            case 5: 
                inicio_sesion(contadorArg, contadorBra, contadorChi)

def menu_GestionAerolineas(contadorArg, contadorBra, contadorChi):
    limpiar_pantalla()

    def gestionAerolineas_Crear(contadorArg, contadorBra, contadorChi):
        limpiar_pantalla()

        def submenu_CreacionAerolineas(contadorArg, contadorBra, contadorChi):
            limpiar_pantalla()

            opcion5 = 1
            while(opcion5 != 0):
                print("1. Cargar otra Aerolinea")
                print("2. Ver Cantidad de Aerolineas cargadas")
                print("3. Volver al menu principal")

                opcion5 = int(input("Seleccion de opcion: "))
                while(opcion5 < 1 or opcion5 > 3):
                    opcion5 = int(input("Opcion invalida, intente nuevamente: "))
                match opcion5:
                    case 1: 
                        gestionAerolineas_Crear(contadorArg, contadorBra, contadorChi)
                    case 2: 
                        submenu_mostrarAerolineas(contadorArg, contadorBra, contadorChi)
                    case 3: 
                        menu_GestionNovedades(codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                                              codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                                              codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)
        
        def submenu_mostrarAerolineas(contadorArg, contadorBra, contadorChi):
            limpiar_pantalla()

            opcion6 = 1

            if(contadorArg > contadorChi and contadorArg > contadorBra):
                if(contadorChi > contadorBra):
                    print(f"El pais con mayor cantidad de Aerolineas es Argentina con: {contadorArg} cargadas, seguido de Chile con: {contadorChi} y por ultimo Brasil con: {contadorBra}")
                else:
                    print(f"El pais con mayor cantidad de Aerolineas es Argentina con: {contadorArg} cargadas, seguido de Brasil con: {contadorBra} y por ultimo Chile con: {contadorChi}")
                    
            if(contadorBra > contadorArg and contadorBra > contadorChi):
                if(contadorArg > contadorChi):
                    print(f"El pais con mayor cantidad de Aerolineas es Brasil con: {contadorBra} cargadas, seguido de Argentina con: {contadorArg} y por ultimo Chile con: {contadorChi}")
                else:
                    print(f"El pais con mayor cantidad de Aerolineas es Brasil con: {contadorBra} cargadas, seguido de Chile con: {contadorChi} y por ultimo Argentina con: {contadorArg}")

            if(contadorChi > contadorArg and contadorChi > contadorBra):
                if(contadorArg > contadorBra):
                    print(f"El pais con mayor cantidad de Aerolineas es Chile con: {contadorChi} cargadas, seguido de Argentina con: {contadorArg} y por ultimo Brasil con: {contadorBra}")
                else:
                    print(f"El pais con mayor cantidad de Aerolineas es Chile con: {contadorChi} cargadas, seguido de Brasil con: {contadorBra} y por ultimo Argentina con: {contadorArg}")

            if(contadorArg == contadorBra and contadorArg == contadorChi):
                print(f"Los tres paises tienen la misma cantidad de Aerolineas cargadas con: {contadorArg} cada uno")

            while(opcion6 != 0):
                print("1. Volver al menu de carga de Aerolineas")
                print("2. Volver al menu principal")

                opcion6 = int(input("Seleccion de opcion: "))
                while(opcion6 < 1 or opcion6 > 2):
                    opcion6 = int(input("Opcion invalida, intente nuevamente: "))
                match opcion6:
                    case 1: 
                        gestionAerolineas_Crear(contadorArg, contadorBra, contadorChi)
                    case 2: 
                        menu_principal(contadorArg, contadorBra, contadorChi,
                                       codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                                       codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                                       codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)

        nombreAerolinea = input("Inserte nombre aerolinea:")

        codigoIATA = input("Ingrese codigo IATA:")

        if(len(codigoIATA) <= 3 and codigoIATA.isalpha()):
            descripcionAerolinea = input("Ingrese descripcion de vuelo:")
            codigoPais = input("Ingrese el pais de las opciones: ARG (Argentina), BRA (Brasil) o CHI (Chile):")

            match codigoPais:
                case "ARG": 
                    contadorArg = contadorArg + 1
                    print("\nAerolinea cargada exitosamente.")
                    time.sleep(3)
                    submenu_CreacionAerolineas(contadorArg, contadorBra, contadorChi)
                case "BRA": 
                    contadorBra = contadorBra + 1
                    print("\nAerolinea cargada exitosamente.")
                    time.sleep(3)
                    submenu_CreacionAerolineas(contadorArg, contadorBra, contadorChi)
                case "CHI": 
                    contadorChi = contadorChi + 1
                    print("\nAerolinea cargada exitosamente.")
                    time.sleep(3)
                    submenu_CreacionAerolineas(contadorArg, contadorBra, contadorChi)
                case _: 
                    print("\nPais invalido, intente nuevamente")
                    time.sleep(3)
                    limpiar_pantalla()
                    gestionAerolineas_Crear(contadorArg, contadorBra, contadorChi)
        else:
            print("\nCodigo IATA invalido, intente nuevamente")
            time.sleep(3)
            limpiar_pantalla()
            gestionAerolineas_Crear(contadorArg, contadorBra, contadorChi)

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
            case 1: 
                gestionAerolineas_Crear(contadorArg, contadorBra, contadorChi)
            case 2: 
                cartel_desarrollo()
            case 3: 
                cartel_desarrollo()
            case 4: 
                menu_principal(contadorArg, contadorBra, contadorChi, 
                               codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                               codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                               codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)

def menu_GestionNovedades(codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                          codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                          codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3):
    limpiar_pantalla()
        
    def gestionNovedades_Editar():
        cartel_desarrollo()
    
    def gestionNovedades_Ver(codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                             codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                             codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3):
        limpiar_pantalla()

        print(f"Novedad: {codigoNovedad1} Fecha: {fechaPublicacionNovedad1} Valido hasta: {fechaExpiracionNovedad1}\n {textoNovedad1}")
        print(f"Novedad: {codigoNovedad2} Fecha: {fechaPublicacionNovedad2} Valido hasta: {fechaExpiracionNovedad2}\n {textoNovedad2}")
        print(f"Novedad: {codigoNovedad3} Fecha: {fechaPublicacionNovedad3} Valido hasta: {fechaExpiracionNovedad3}\n {textoNovedad3}")

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
            case 1: 
                cartel_desarrollo()
            case 2: 
                gestionNovedades_Editar()
            case 3: 
                cartel_desarrollo()
            case 4: 
                gestionNovedades_Ver(codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                                     codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                                     codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)
            case 5: 
                menu_principal(contadorArg, contadorBra, contadorChi, codigoNovedad1, 
                               textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                               codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                               codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)
                
def menu_Reportes():
    limpiar_pantalla()

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
            case 1: 
                cartel_desarrollo()
            case 2: 
                cartel_desarrollo()
            case 3: 
                cartel_desarrollo()
            case 4: 
                menu_GestionNovedades(codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
                                      codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
                                      codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)
inicio_sesion(contadorArg, contadorBra, contadorChi, 
              codigoNovedad1, textoNovedad1, fechaPublicacionNovedad1, fechaExpiracionNovedad1, 
              codigoNovedad2, textoNovedad2, fechaPublicacionNovedad2, fechaExpiracionNovedad2,
              codigoNovedad3, textoNovedad3, fechaPublicacionNovedad3, fechaExpiracionNovedad3)