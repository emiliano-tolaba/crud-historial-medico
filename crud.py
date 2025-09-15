import os
import csv
import time

# Lista principal para almacenar los pacientes
pacientes = []

# Función para limpiar la pantalla de la consola y mejorar la visualización del programa.
# Usa el comando 'cls' si el sistema operativo es Windows, y 'clear' si es Unix/Linux/Mac.
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para pausar la ejecución
def pausar_pantalla():
    input("\nPresiona Enter para continuar...")

# Función para mostrar un paciente. Recibe el ID del paciente como parámetro
def mostrar_un_paciente(id_paciente):
        paciente = pacientes[id_paciente]
        print(f"ID: {id_paciente} | Nombre: {paciente[0]} | Teléfono: {paciente[1]} | Email: {paciente[2]} | Diagnóstico: {paciente[3]} | Tratamiento: {paciente[4]}")

# Función que verifica si el ID ingresado corresponde a un paciente existente en la lista.
# Recibe por parámetro el ID del paciente
# Retorna True si el ID está dentro del rango válido (mayor o igual a 0 y menor que la cantidad de pacientes).
def validar_id_paciente(id):
    if id > -1 and id < len(pacientes):     
        return True                         

# Función para mostrar todos los pacientes
def mostrar_pacientes():
    limpiar_pantalla()
    print("╔════════════════════════════════════╗")
    print("║  ****** LISTA DE PACIENTES ******  ║")
    print("╚════════════════════════════════════╝\n")

    for i, _ in enumerate(pacientes): # El segundo valor (el paciente) no se utiliza directamente en este bloque, por eso se reemplaza con "_" como convención para variables ignoradas.                    
        mostrar_un_paciente(i)

# Función para crear un nuevo paciente. Se piden los datos personales y se asignan los datos medicos sin definir
def crear_paciente():
    limpiar_pantalla()

    print("╔════════════════════════════════════╗")
    print("║    ****** CREAR PACIENTE ******    ║")
    print("╚════════════════════════════════════╝\n")

    nombre = input("Ingrese el nombre del paciente: ")
    telefono = input("Ingrese el teléfono del paciente: ")
    email = input("Ingrese el email del paciente: ")
    
    # Se agregan campos vacíos para diagnóstico y tratamiento
    pacientes.append([nombre, telefono, email, "Sin definir", "Sin definir"])
    
    print("\nPaciente creado exitosamente.")
    pausar_pantalla()

# Función para modificar paciente. Permite acceder a las opciones "actualizar" y "eliminar" paciente
def modificar_paciente():
    limpiar_pantalla()
    print("╔════════════════════════════════════╗")
    print("║  ****** MODIFICAR PACIENTE ******  ║")
    print("╚════════════════════════════════════╝\n")
    
    nombre = input("Ingrese el nombre del paciente que desea modificar: ")
    encontrado = False                                          # Flag que indica si se encontró el paciente

    for i, paciente in enumerate(pacientes):                    # Se recorre la lista con enumerate para obtener tanto el índice como el paciente.
        if paciente[0].lower() == nombre.lower():               # Si el nombre coincide (ignorando mayúsculas/minúsculas), se muestra la información,
            print(f"\nPaciente encontrado - ID: {i}")           # se accede al submenú del paciente y se marca como encontrado para evitar seguir buscando.
            mostrar_un_paciente(i)
            mostrarSubmenu_paciente(i)                          # muestra el submenu con las opciones actualizar o eliminar
            encontrado = True
            break

    if not encontrado:
        print("\nPaciente no encontrado. Se mostrará la lista completa")    # Si no se encuentra al paciente se muestra la lista completa
        pausar_pantalla()
        mostrar_pacientes()

        try:                        # Se intenta convertir la entrada a entero; si no es válida (por ejemplo, letras), se captura el error con try-except.
            id_paciente = int(input("\nIngrese el ID del paciente que desea seleccionar: "))    
            if validar_id_paciente(id_paciente):            # Valida que exista el ID en la lista
                mostrarSubmenu_paciente(id_paciente)
            else:
                print("ID inválido.")
                pausar_pantalla()
        except ValueError:          # Si ocurre un ValueError (entrada no convertible a entero), se muestra un mensaje y se vuelve al menú principal.
            print("Entrada inválida. Volviendo al menu principal")
            pausar_pantalla()
            
    

# Submenú para opciones de paciente (actualizar y eliminar)
# Recibe por parámetro el ID del paciente
def mostrarSubmenu_paciente(id_paciente):
    while True:
        limpiar_pantalla()
        print("╔════════════════════════════════════╗")
        print("║******* PACIENTE SELECCIONADO ******║")
        print("╚════════════════════════════════════╝\n")
        
        mostrar_un_paciente(id_paciente)
        print("\n1. Actualizar paciente \n2. Eliminar paciente \n3. Volver atrás")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            actualizar_paciente(id_paciente)
        elif opcion == "2":
            eliminar_paciente(id_paciente)
            break
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
        
        #pausar_pantalla()

# Submenú para actualizar datos del paciente
# Recibe por parámetro el ID del paciente
def actualizar_paciente(id_paciente):
    while True:
        limpiar_pantalla()
        print("╔═════════════════════════════════════╗")
        print("║  ****** ACTUALIZAR PACIENTE ******  ║ ")
        print("╚═════════════════════════════════════╝\n")
        mostrar_un_paciente(id_paciente)

        print("\n1. Datos personales\n2. Datos médicos\n3. Volver atrás")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            actualizar_datos_personales(id_paciente)                        # modifica solo los datos personales
        elif opcion == "2":
            actualizar_datos_medicos(id_paciente)                           # modifica solo los datos medicos
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
        

# Elimina un paciente de la lista según su ID, previa confirmación del usuario.
# Muestra un mensaje de confirmación y, si el usuario acepta, elimina al paciente y pausa la pantalla.
def eliminar_paciente(id_paciente):
    # Solicita confirmación al usuario antes de eliminar
    confirmar = input("¿Está seguro que desea eliminar este paciente? (s/n): ")
    
    # Si la respuesta es afirmativa (sin importar mayúsculas/minúsculas)
    if confirmar.lower() == "s":
        pacientes.pop(id_paciente)                  # Elimina al paciente de la lista usando su índice
        print("Paciente eliminado.")
        pausar_pantalla()
    else:
        print("Eliminacion cancelada.")
        pausar_pantalla()

# Submenú para actualizar datos personales
# Recibe por parámetro el ID del paciente
def actualizar_datos_personales(id_paciente):
    while True:
        limpiar_pantalla()
        print("╔═════════════════════════════════════════════╗")
        print("║  ****** ACTUALIZAR DATOS PERSONALES ******  ║ ")
        print("╚═════════════════════════════════════════════╝\n")
        mostrar_un_paciente(id_paciente)
        print("\n1. Nombre\n2. Teléfono\n3. Email\n4. Volver atrás")
        
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            pacientes[id_paciente][0] = input("Nuevo nombre: ")
            print("Se ha actualizado el dato del paciente")
            pausar_pantalla()
        elif opcion == "2":
            pacientes[id_paciente][1] = input("Nuevo teléfono: ")
            print("Se ha actualizado el dato del paciente")
            pausar_pantalla()
        elif opcion == "3":
            pacientes[id_paciente][2] = input("Nuevo email: ")
            print("Se ha actualizado el dato del paciente")
            pausar_pantalla()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Submenú para actualizar datos médicos
# Recibe por parámetro el ID del paciente
def actualizar_datos_medicos(id_paciente):
    while True:
        limpiar_pantalla()
        print("╔═════════════════════════════════════════════╗")
        print("║    ****** ACTUALIZAR DATOS MÉDICOS ******   ║ ")
        print("╚═════════════════════════════════════════════╝\n")
        mostrar_un_paciente(id_paciente)
        print("\n1. Diagnóstico\n2. Tratamiento\n3. Volver atrás")        
        
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            pacientes[id_paciente][3] = input("Nuevo diagnóstico: ")
            print("Se ha actualizado el dato del paciente")
            pausar_pantalla()
        elif opcion == "2":
            pacientes[id_paciente][4] = input("Nuevo tratamiento: ")
            print("Se ha actualizado el dato del paciente")
            pausar_pantalla()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# Guarda la lista completa de pacientes en un archivo CSV llamado 'agenda_medica.csv'.
# Se usa codificación UTF-8 para asegurar compatibilidad con caracteres especiales.
def guardar_agenda():
    with open("agenda_medica.csv", "w", newline='', encoding='utf-8') as archivo:       # Cada paciente se escribe como una fila, manteniendo el orden de los campos: nombre, teléfono, email, diagnóstico y tratamiento.
        escritor = csv.writer(archivo)
        for paciente in pacientes:
            escritor.writerow(paciente)

    print("\nAgenda guardada exitosamente!")
    pausar_pantalla()

# Recupera la agenda médica desde el archivo CSV 'agenda_medica.csv'.
def recuperar_agenda():
    try:
        with open("agenda_medica.csv", "r", encoding='utf-8') as archivo:   # Abre el archivo en modo lectura con codificación UTF-8 para soportar caracteres especiales.
            lector = csv.reader(archivo)                                    # Crea un objeto lector que permite recorrer el archivo CSV línea por línea, interpretando cada fila como una lista de valores separados por comas.
            pacientes.clear()                                               # Limpia la lista actual de pacientes
            for fila in lector:                                             # Carga cada fila del archivo como un nuevo paciente.
                pacientes.append(fila)
        print("\nAgenda recuperada exitosamente!")
    except FileNotFoundError:                           # Si el archivo no existe (por ejemplo, en la primera ejecución), se captura el error y se informa al usuario.
        print("\nNo se encontró una agenda guardada previamente.")
    
    pausar_pantalla()

# Programa principal con menú interactivo
while True:
    limpiar_pantalla()
    print("╔════════════════════════════════════╗")
    print("║   ****** HISTORIAL MÉDICO ******   ║ ")
    print("╚════════════════════════════════════╝\n")
    print("1. Crear paciente\n2. Modificar paciente\n3. Mostrar lista pacientes\n4. Guardar agenda en CSV\n5. Recuperar última agenda guardada\n6. Salir")    
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        crear_paciente()
    elif opcion == "2":
        modificar_paciente()
    elif opcion == "3":
        mostrar_pacientes()
        pausar_pantalla()
    elif opcion == "4":
        guardar_agenda()
    elif opcion == "5":
        recuperar_agenda()
    elif opcion == "6":
        print("\nSaliendo del programa...")
        time.sleep(1)
        break
    else:
        print("\nOpción inválida.")
        pausar_pantalla()
