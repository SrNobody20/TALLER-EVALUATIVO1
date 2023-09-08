
agrupaciones = []
def registrar_agrupacion():
    id = input("Ingrese el ID de la agrupación: ")
    nombre = input("Ingrese el nombre de la agrupación: ")
    genero = input("Ingrese el género de la agrupación: ")
    hora_presentacion = input("Ingrese la hora de presentación (en formato HH:MM): ")
    pago = float(input("Ingrese el pago para la agrupación: "))
    estado = int(input("Ingrese el estado de la banda (True=1/False=0): "))
    agrupacion = {"id": id, "nombre": nombre, "genero": genero, "hora_presentacion": hora_presentacion, "pago": pago, "estado": estado}
    agrupaciones.append(agrupacion)
    print("Agrupación registrada con éxito.")

def mostrar_no_presentadas():
    print("Agrupaciones que no se han presentado:")
    bandas_no_presentadas = 0  
    for agrupacion in agrupaciones:
        if not agrupacion['estado']:
            print(f"ID: {agrupacion['id']}, Nombre: {agrupacion['nombre']}, Hora de presentación: {agrupacion['hora_presentacion']} - No se ha presentado.")
            bandas_no_presentadas = 1
    if not bandas_no_presentadas:
        print("Todas las bandas ya se han presentado.")


def cambiar_hora_presentacion():
    id_buscar = input("Ingrese el ID de la agrupación cuya hora de presentación desea cambiar: ")
    nueva_hora = input("Ingrese la nueva hora de presentación (en formato HH:MM): ")
    for agrupacion in agrupaciones:
        if agrupacion["id"] == id_buscar and not agrupacion["estado"]:
            agrupacion["hora_presentacion"] = nueva_hora
            print("Hora de presentación actualizada con éxito.")
            return
    print("No se encontró la agrupación o ya se ha presentado.")

def retirar_agrupacion():
    id_retirar = input("Ingrese el ID de la agrupación que desea retirar: ")
    for agrupacion in agrupaciones:
        if agrupacion["id"] == id_retirar and not agrupacion["estado"]:
            agrupaciones.remove(agrupacion)
            print("Agrupación retirada con éxito.")
            return
    print("No se encontró la agrupación o ya se ha presentado.")

while True:
    print("\nMenú del Festival de Música:")
    print("1. Registrar agrupación")
    print("2. Mostrar agrupaciones no presentadas")
    print("3. Cambiar hora de presentación")
    print("4. Retirar agrupación")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    
    if opcion == "1":
        registrar_agrupacion()
    elif opcion == "2":
        mostrar_no_presentadas()
    elif opcion == "3":
        cambiar_hora_presentacion()
    elif opcion == "4":
        retirar_agrupacion()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")
