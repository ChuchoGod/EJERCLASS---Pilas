# Simular acciones de un editor de texto
acciones = []

# Función para realizar una acción
def realizar_accion(accion):
    acciones.append(accion)
    print(f"Acción realizada: {accion}")

# Función para deshacer la última acción
def deshacer_accion():
    if len(acciones) == 0:
        print("No hay más acciones para deshacer.")
    else:
        accion_deshacer = acciones.pop()
        print(f"Acción deshecha: {accion_deshacer}")

# Realizando algunas acciones
realizar_accion("Escribir 'Hola'")
realizar_accion("Escribir 'Mundo'")
realizar_accion("Eliminar palabra 'Mundo'")

print("Estado de las acciones:", acciones)

# Deshacer las últimas dos acciones
deshacer_accion()
deshacer_accion()

print("Estado de las acciones después de deshacer:", acciones)
