# ============================================================
#   GUÍA DE REPASO - MÓDULO 1: Fundamentos de Python
#   Prueba de Desempeño - Riwi
#   Temas: Variables, Operadores, Control, Funciones,
#          Estructuras de datos, Errores, Buenas prácticas
# ============================================================


# ============================================================
# TEMA 1: VARIABLES Y TIPOS DE DATOS
# ============================================================

# Un entero (número sin decimales)
edad = 20

# Un flotante (número con decimales)
altura = 1.75

# Una cadena de texto (string)
nombre = "Jhosep"

# Un booleano (True o False)
es_estudiante = True

# Imprimir los valores con sus tipos
print("=" * 40)
print("TEMA 1: VARIABLES Y TIPOS DE DATOS")
print("=" * 40)
print(nombre, "tiene", edad, "años")
print("¿Es estudiante?", es_estudiante)
print("Tipo de 'edad':", type(edad))
print("Tipo de 'altura':", type(altura))


# ============================================================
# TEMA 2: OPERADORES ARITMÉTICOS Y LÓGICOS
# ============================================================

print("\n" + "=" * 40)
print("TEMA 2: OPERADORES")
print("=" * 40)

precio = 50000
descuento = 10000

# Operadores aritméticos
total = precio - descuento
print("Total a pagar:", total)
print("El doble del total:", total * 2)
print("Mitad del total:", total / 2)
print("Residuo de 100 / 3:", 100 % 3)

# Operadores lógicos (and, or, not)
tiene_dinero = True
tiene_cupo = False

# and: ambas condiciones deben ser True
print("¿Puede comprar?", tiene_dinero and tiene_cupo)

# or: al menos una debe ser True
print("¿Tiene algo?", tiene_dinero or tiene_cupo)

# not: invierte el valor booleano
print("¿No tiene cupo?", not tiene_cupo)


# ============================================================
# TEMA 3: ESTRUCTURAS DE CONTROL
# ============================================================

print("\n" + "=" * 40)
print("TEMA 3: ESTRUCTURAS DE CONTROL")
print("=" * 40)

# --- Condicional if / elif / else ---
nota = 75

if nota >= 90:
    print("Resultado: Excelente")
elif nota >= 70:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")

# --- Bucle for: recorre una lista ---
print("\nFrutas disponibles:")
frutas = ["mango", "pera", "uva"]

for fruta in frutas:
    print(" -", fruta)

# --- Bucle while con break y continue ---
print("\nContador (salta el 5, para en el 8):")
contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        continue  # Salta este número, no lo imprime

    if contador == 8:
        break     # Detiene el bucle aquí

    print(" Contador:", contador)


# ============================================================
# TEMA 4: FUNCIONES
# ============================================================

print("\n" + "=" * 40)
print("TEMA 4: FUNCIONES")
print("=" * 40)

# Función que recibe dos números y retorna su suma
def sumar(a, b):
    resultado = a + b
    return resultado

total_suma = sumar(10, 25)
print("Suma de 10 + 25:", total_suma)


# Función con valor por defecto en un parámetro
def saludar(nombre, saludo="Hola"):
    print(saludo + ", " + nombre + "!")

saludar("Jhosep")             # Usa "Hola" por defecto
saludar("Jhosep", "Buenas")  # Usa "Buenas"


# Función lambda: función corta en una sola línea
cuadrado = lambda x: x ** 2
print("Cuadrado de 5:", cuadrado(5))


# ============================================================
# TEMA 5: ESTRUCTURAS DE DATOS
# ============================================================

print("\n" + "=" * 40)
print("TEMA 5: ESTRUCTURAS DE DATOS")
print("=" * 40)

# --- LISTAS (se pueden modificar) ---
print("\n-- Lista --")
estudiantes = ["Ana", "Luis", "Jhosep"]

estudiantes.append("María")    # Agregar al final
estudiantes.remove("Luis")     # Eliminar un elemento
print("Estudiantes:", estudiantes)
print("Primero:", estudiantes[0])  # Acceder por índice

# --- TUPLAS (NO se pueden modificar) ---
print("\n-- Tupla --")
coordenadas = (4.8, -74.0)  # Latitud y longitud
print("Latitud:", coordenadas[0])
print("Longitud:", coordenadas[1])

# --- DICCIONARIOS (clave: valor) ---
print("\n-- Diccionario --")
persona = {
    "nombre": "Jhosep",
    "edad": 20,
    "ciudad": "Barranquilla"
}

print("Nombre:", persona["nombre"])
persona["edad"] = 21              # Modificar un valor existente
persona["profesion"] = "Coder"   # Agregar una nueva clave
print("Persona actualizada:", persona)


# ============================================================
# TEMA 6: MANEJO DE ERRORES
# ============================================================

print("\n" + "=" * 40)
print("TEMA 6: MANEJO DE ERRORES")
print("=" * 40)

# try/except evita que el programa se caiga con datos incorrectos
def pedir_numero():
    try:
        numero = int(input("Ingresa un número entero: "))
        print("El doble es:", numero * 2)
    except ValueError:
        # ValueError ocurre cuando el texto no se puede convertir a entero
        print("Error: debes ingresar un número válido, no texto.")

pedir_numero()


# ============================================================
# TEMA 7: CASO DE ESTUDIO COMPLETO
#         (Une todos los temas anteriores)
# ============================================================

print("\n" + "=" * 40)
print("TEMA 7: CASO DE ESTUDIO COMPLETO")
print("Sistema de Registro de Estudiantes")
print("=" * 40)

# Lista global donde guardamos los estudiantes
registro = []

# Función para registrar un estudiante
def registrar_estudiante(nombre, nota):
    # Guardamos cada estudiante como un diccionario
    estudiante = {
        "nombre": nombre,
        "nota": nota
    }
    registro.append(estudiante)
    print(f"  ✔ '{nombre}' registrado con nota {nota}.")

# Función para calcular el promedio del grupo
def calcular_promedio():
    if len(registro) == 0:
        return 0
    suma_notas = 0
    for est in registro:
        suma_notas += est["nota"]
    return suma_notas / len(registro)

# Función para mostrar los resultados finales
def mostrar_resultados():
    print("\n--- RESULTADOS FINALES ---")
    for est in registro:
        nombre = est["nombre"]
        nota = est["nota"]

        # Determinamos el estado según la nota
        if nota >= 90:
            estado = "Excelente"
        elif nota >= 70:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"  {nombre}: {nota} -> {estado}")

    promedio = calcular_promedio()
    print(f"\nPromedio del grupo: {promedio:.2f}")

# Función principal que controla todo el programa
def main():
    print("\n=== Sistema de Registro ===")

    # Pedimos cuántos estudiantes se van a ingresar
    try:
        cantidad = int(input("¿Cuántos estudiantes vas a registrar? "))
    except ValueError:
        print("Error: ingresa un número válido.")
        return  # Salimos si el dato es incorrecto

    # Bucle para registrar cada estudiante uno por uno
    for i in range(cantidad):
        nombre = input(f"\nNombre del estudiante {i + 1}: ")

        try:
            nota = float(input(f"Nota de {nombre} (0-100): "))
        except ValueError:
            print("Nota inválida. Se asignará 0.")
            nota = 0

        registrar_estudiante(nombre, nota)

    # Mostramos todos los resultados al finalizar
    mostrar_resultados()

# Punto de entrada del programa
main()
