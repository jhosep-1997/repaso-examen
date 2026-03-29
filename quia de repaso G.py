"""
GUÍA DE PREPARACIÓN - PRUEBA DE DESEMPEÑO M1
Nombre del Coder: Jhosep Ahumada / William Rojas
Temas: Fundamentos de Python (Variables, Control, Funciones, Errores)
"""

# --- 1. ESTRUCTURAS DE DATOS Y LAMBDAS ---
# Uso de listas y diccionarios para gestionar información [cite: 18]
db_usuarios = []

# Función lambda para cálculos rápidos (mencionado en el PDF) [cite: 17]
# Ejemplo: Calcular un descuento del 10%
aplicar_descuento = lambda precio: precio * 0.90


# --- 2. FUNCIONES Y MODULARIZACIÓN [cite: 17, 20] ---

def validar_entrada_numero(mensaje):
    """
    MANEJO DE ERRORES: Esta función asegura que el programa no se detenga
    si el usuario ingresa texto en lugar de números[cite: 19].
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("❌ Error: Por favor, ingrese un número válido.")


def registrar_dato():
    """
    Simulación de análisis y diseño de solución para un problema real[cite: 28, 29].
    """
    print("\n--- Registro de Nuevo Elemento ---")
    nombre = input("Ingrese el nombre: ").strip()
    
    # Uso de la función de validación
    precio = validar_entrada_numero("Ingrese el precio base: ")
    
    # Lógica con condicionales [cite: 16]
    precio_final = aplicar_descuento(precio) if precio > 100 else precio
    
    item = {
        "id": len(db_usuarios) + 1,
        "nombre": nombre,
        "precio_final": precio_final
    }
    
    db_usuarios.append(item)
    print(f"✅ Registro exitoso: {nombre} procesado.")


def mostrar_reporte():
    """
    Uso de bucles for y f-strings para presentar resultados[cite: 16, 31].
    """
    if not db_usuarios:
        print("\n⚠️ No hay datos registrados para mostrar.")
        return

    print("\n--- REPORTE TÉCNICO ---")
    print(f"{'ID':<5} | {'NOMBRE':<15} | {'PRECIO FINAL':<10}")
    print("-" * 35)
    
    for user in db_usuarios:
        print(f"{user['id']:<5} | {user['nombre']:<15} | ${user['precio_final']:<10.2f}")


# --- 3. ESTRUCTURA DE CONTROL PRINCIPAL [cite: 16] ---

def ejecutar_sistema():
    """
    Punto de entrada que simula la ejecución técnica de la prueba[cite: 35].
    """
    while True:
        print("\n--- MENÚ DE PRUEBA DE DESEMPEÑO ---")
        print("1. Registrar información")
        print("2. Ver reporte de resultados")
        print("3. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_dato()
        elif opcion == "2":
            mostrar_reporte()
        elif opcion == "3":
            print("Finalizando programa. ¡Prepárate para la sustentación! [cite: 38]")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del script
if __name__ == "__main__":
    ejecutar_sistema()