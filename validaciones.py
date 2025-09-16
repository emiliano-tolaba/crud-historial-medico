# Función que verifica si el ID ingresado corresponde a un paciente existente en la lista.
# Recibe por parámetro el ID del paciente
# Retorna True si el ID está dentro del rango válido (mayor o igual a 0 y menor que la cantidad de pacientes).
def validar_id_paciente(id, lista_pacientes):
    if id > -1 and id < len(lista_pacientes):     
        return True  

# Valida que el texto ingresado sea adecuado para campos como nombre o diagnóstico.
# La función retorna True si:
# - El texto no está vacío ni compuesto solo por espacios.
# - Todos los caracteres son letras o espacios (no se permiten números ni símbolos).
def validar_texto(cadena):
    return cadena.strip() != "" and all(caracter.isalpha() or caracter.isspace() for caracter in cadena)

# Validación de teléfono: debe contener solo dígitos
def validar_telefono(telefono):
    return telefono.isdigit()

# Validación de email: debe contener "@" y "."
def validar_email(email):
    return "@" in email and "." in email

# Verifica si hay pacientes cargados en la lista.
def validar_pacientes_cargados(lista_pacientes):
    return len(lista_pacientes) > 0

# Solicita al usuario que confirme una acción (como eliminar, salir, etc.).
# Retorna True si el usuario responde "s" (sí), False en cualquier otro caso.
def confirmar_accion(mensaje="¿Está seguro que desea continuar? (s/n): "):
    respuesta = input(mensaje)
    return respuesta.strip().lower() == "s"
