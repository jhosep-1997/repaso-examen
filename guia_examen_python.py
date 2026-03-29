# ================================
# GUÍA PARA EXAMEN - PYTHON MÓDULO 1
# Basado en la guía de Riwi
# ================================

# Lista global donde guardamos los usuarios
usuarios = []

# ================================
# FUNCIONES DE USUARIOS
# ================================

def registrar_usuario():
    """
    Permite registrar un usuario con validación de datos
    """
    nombre = input("Ingrese su nombre: ").strip()

    if nombre == "":
        print("Error: El nombre no puede estar vacío")
        return

    try:
        edad = int(input("Ingrese su edad: "))

        if edad <= 0:
            print("Error: Edad inválida")
            return

    except ValueError:
        print("Error: Debes ingresar un número")
        return

    usuario = {
        "nombre": nombre,
        "edad": edad
    }

    usuarios.append(usuario)

    print("Usuario registrado correctamente")


def mostrar_usuarios():
    """
    Muestra todos los usuarios registrados
    """
    if len(usuarios) == 0:
        print("No hay usuarios registrados")
        return

    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. Nombre: {usuario['nombre']} - Edad: {usuario['edad']}")


# ================================
# FUNCIÓN DE TIENDA (PROBLEMA REAL)
# ================================

def calcular_total():
    """
    Calcula el total de una compra con descuento
    """
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))

        if precio <= 0 or cantidad <= 0:
            print("Valores inválidos")
            return

    except ValueError:
        print("Error en los datos")
        return

    total = precio * cantidad

    if total > 100:
        descuento = total * 0.10
        total -= descuento
        print("Se aplicó un descuento del 10%")

    print(f"Total a pagar: {total}")


# ================================
# FUNCIONES CON LISTAS
# ================================

numeros = []

def agregar_numero():
    try:
        num = int(input("Ingrese un número: "))
        numeros.append(num)
    except ValueError:
        print("Error: Debe ser número")


def mostrar_promedio():
    if len(numeros) == 0:
        print("No hay números")
        return

    promedio = sum(numeros) / len(numeros)
    print(f"Promedio: {promedio}")


# ================================
# MENÚ PRINCIPAL
# ================================

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Calcular compra")
        print("4. Agregar número")
        print("5. Mostrar promedio")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            mostrar_usuarios()

        elif opcion == "3":
            calcular_total()

        elif opcion == "4":
            agregar_numero()

        elif opcion == "5":
            mostrar_promedio()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


# Ejecutar programa
menu()
