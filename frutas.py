
frutas = []

n = int(input("Ingrese la cantidad de frutas para el salpicón: "))

for i in range(1, n + 1):
    print(f"Ingrese la información de la fruta #{i}:")
    id_fruta = input("ID de la fruta: ")
    nombre_fruta = input("Nombre de la fruta: ")
    precio_unitario = float(input("Precio unitario de la fruta: "))
    cantidad = int(input("Cantidad de la fruta: "))

    fruta = {
        "ID": id_fruta,
        "Nombre": nombre_fruta,
        "Precio Unitario": precio_unitario,
        "Cantidad": cantidad
    }

    frutas.append(fruta)

costo_total = sum(fruta["Precio Unitario"] * fruta["Cantidad"] for fruta in frutas)

print("\nSalpicón de frutas:")
for fruta in frutas:
    print(f"ID: {fruta['ID']}, Nombre: {fruta['Nombre']}, Precio Unitario: ${fruta['Precio Unitario']:.2f}, Cantidad: {fruta['Cantidad']}")
print(f"Costo Total del Salpicón: ${costo_total:.2f}")
