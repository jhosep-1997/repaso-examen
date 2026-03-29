# ============================================================
#   EXPLICACIÓN COMPLETA - MÓDULO 1: Fundamentos de Python
#   Prueba de Desempeño - Riwi
#   Aquí encontrarás la explicación + ejemplo de cada tema
# ============================================================


# ============================================================
# TEMA 1: VARIABLES Y TIPOS DE DATOS
# ------------------------------------------------------------
# Una variable es como una cajita con nombre donde guardas
# información. Python detecta el tipo de dato automáticamente.
# ============================================================

edad = 20           # int   → número entero (sin decimales)
altura = 1.75       # float → número con decimales
nombre = "Jhosep"   # str   → texto (siempre entre comillas)
activo = True       # bool  → solo puede ser True o False

print("=" * 50)
print("TEMA 1: VARIABLES Y TIPOS DE DATOS")
print("=" * 50)
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Activo?:", activo)
print("Tipo de edad:", type(edad))
print("Tipo de nombre:", type(nombre))


# ============================================================
# TEMA 2: OPERADORES ARITMÉTICOS Y LÓGICOS
# ------------------------------------------------------------
# Aritméticos → hacen cálculos matemáticos
# Lógicos     → combinan condiciones True/False
# ============================================================

print("\n" + "=" * 50)
print("TEMA 2: OPERADORES")
print("=" * 50)

# Operadores aritméticos
print("10 + 3 =", 10 + 3)    # suma        → 13
print("10 - 3 =", 10 - 3)    # resta       → 7
print("10 * 3 =", 10 * 3)    # multiplicar → 30
print("10 / 3 =", 10 / 3)    # división    → 3.33
print("10 % 3 =", 10 % 3)    # residuo     → 1 (lo que sobra)
print("2 ** 3 =", 2 ** 3)    # potencia    → 8

# Operadores lógicos
tiene_dinero = True
tiene_cupo   = False

# and → ambas condiciones deben ser True para dar True
print("\nand (ambas True):", tiene_dinero and tiene_cupo)  # False

# or → al menos una debe ser True para dar True
print("or  (una True):", tiene_dinero or tiene_cupo)       # True

# not → invierte el valor booleano
print("not (invierte):", not tiene_cupo)                   # True


# ============================================================
# TEMA 3: ESTRUCTURAS DE CONTROL
# ------------------------------------------------------------
# Le dicen al programa QUÉ HACER según una condición,
# o REPETIR algo varias veces.
# ============================================================

print("\n" + "=" * 50)
print("TEMA 3: ESTRUCTURAS DE CONTROL")
print("=" * 50)

# --- IF / ELIF / ELSE ---
# Toma decisiones según una condición
nota = 85

if nota >= 90:
    print("Nota 85 → Excelente")
elif nota >= 70:          # elif = "si no, pero si..."
    print("Nota 85 → Aprobado")
else:                     # else = "en cualquier otro caso"
    print("Nota 85 → Reprobado")

# --- BUCLE FOR ---
# Repite algo una cantidad fija de veces o recorre una lista
print("\nBucle for con range(4):")
for i in range(4):        # range(4) genera: 0, 1, 2, 3
    print("  i =", i)

# --- BUCLE WHILE ---
# Repite MIENTRAS una condición sea True
print("\nBucle while hasta x = 4:")
x = 0
while x < 5:
    print("  x =", x)
    x += 1                # x = x + 1 (importante para no loop infinito)

# --- BREAK y CONTINUE ---
# break    → para el bucle de golpe
# continue → salta esa vuelta y sigue con la siguiente
print("\nBreak (para en 3) y Continue (salta el 2):")
for n in range(6):
    if n == 2:
        continue          # salta el 2
    if n == 4:
        break             # para en el 4
    print("  n =", n)


# ============================================================
# TEMA 4: FUNCIONES
# ------------------------------------------------------------
# Son bloques de código reutilizables.
# Las defines UNA VEZ y las llamas cuando las necesites.
# Sin llamarlas, NO hacen nada por solas.
# ============================================================

print("\n" + "=" * 50)
print("TEMA 4: FUNCIONES")
print("=" * 50)

# Definir una función con parámetros y retorno
def sumar(a, b):
    # a y b son los parámetros (datos que recibe la función)
    resultado = a + b
    return resultado      # return → devuelve el resultado

# Llamar la función y guardar el resultado
total = sumar(10, 25)
print("sumar(10, 25) =", total)

# Función con valor por defecto en un parámetro
def saludar(nombre, saludo="Hola"):
    # Si no se pasa 'saludo', usa "Hola" por defecto
    print(saludo + ", " + nombre + "!")

saludar("Jhosep")              # usa "Hola" por defecto
saludar("Jhosep", "Buenas")   # usa "Buenas"

# Función lambda: función corta en una sola línea
# Útil para operaciones simples
doble = lambda x: x * 2
cuadrado = lambda x: x ** 2

print("doble(5) =", doble(5))
print("cuadrado(4) =", cuadrado(4))


# ============================================================
# TEMA 5: ESTRUCTURAS DE DATOS
# ------------------------------------------------------------
# Sirven para guardar VARIOS datos juntos en una sola variable.
#
# LISTA      → ordenada, modificable            → []
# TUPLA      → ordenada, NO modificable         → ()
# DICCIONARIO → pares clave:valor               → {}
# ============================================================

print("\n" + "=" * 50)
print("TEMA 5: ESTRUCTURAS DE DATOS")
print("=" * 50)

# --- LISTA ---
print("\n-- Lista --")
frutas = ["mango", "pera", "uva"]

frutas.append("banano")    # agregar al final
frutas.remove("pera")      # eliminar un elemento
print("Lista:", frutas)
print("Primera fruta:", frutas[0])   # acceder por posición (empieza en 0)
print("Última fruta:", frutas[-1])   # -1 accede al último

# Recorrer una lista con for
print("Recorriendo lista:")
for fruta in frutas:
    print("  -", fruta)

# --- TUPLA ---
print("\n-- Tupla --")
coordenadas = (4.8, -74.0)   # NO se puede modificar después

print("Latitud:", coordenadas[0])
print("Longitud:", coordenadas[1])
# coordenadas[0] = 5.0  ← esto daría ERROR porque las tuplas no cambian

# --- DICCIONARIO ---
print("\n-- Diccionario --")
persona = {
    "nombre": "Jhosep",
    "edad": 20,
    "ciudad": "Barranquilla"
}

print("Nombre:", persona["nombre"])    # acceder por clave
persona["edad"] = 21                   # modificar un valor
persona["profesion"] = "Coder"         # agregar una clave nueva
print("Diccionario actualizado:", persona)

# Recorrer un diccionario
print("Claves y valores:")
for clave, valor in persona.items():
    print(" ", clave, "→", valor)


# ============================================================
# TEMA 6: MANEJO DE ERRORES
# ------------------------------------------------------------
# Evita que el programa se CAIGA cuando el usuario
# ingresa algo incorrecto o pasa algo inesperado.
#
# try    → "intenta ejecutar esto"
# except → "si falla, haz esto otro"
# ============================================================

print("\n" + "=" * 50)
print("TEMA 6: MANEJO DE ERRORES")
print("=" * 50)

def pedir_numero():
    try:
        # Intentamos convertir lo que escriba el usuario a entero
        numero = int(input("Ingresa un número entero: "))
        print("El doble es:", numero * 2)

    except ValueError:
        # ValueError ocurre cuando el texto no se puede convertir a int
        print("Error: eso no es un número entero válido.")

pedir_numero()


# ============================================================
# TEMA 7: BUENAS PRÁCTICAS
# ------------------------------------------------------------
# Son hábitos que hacen el código más LEGIBLE y ORDENADO.
# Te dan puntos extra en la sustentación.
#
# ✅ Nombres descriptivos (no x, a, b sueltos)
# ✅ Comentarios que explican el por qué
# ✅ Modularizar: cada tarea en su propia función
# ✅ Un main() que organiza todo el programa
# ============================================================

print("\n" + "=" * 50)
print("TEMA 7: BUENAS PRÁCTICAS - Caso de estudio completo")
print("Sistema de Registro de Estudiantes")
print("=" * 50)

# Lista global donde guardamos todos los estudiantes registrados
registro = []

# ✅ Función con nombre descriptivo y un solo propósito
def registrar_estudiante(nombre, nota):
    # Guardamos cada estudiante como diccionario dentro de la lista
    estudiante = {
        "nombre": nombre,
        "nota": nota
    }
    registro.append(estudiante)
    print(f"  ✔ '{nombre}' registrado con nota {nota}.")

# ✅ Función separada solo para calcular el promedio
def calcular_promedio():
    if len(registro) == 0:
        return 0
    suma = 0
    for est in registro:
        suma += est["nota"]
    return suma / len(registro)

# ✅ Función separada solo para mostrar resultados
def mostrar_resultados():
    print("\n--- RESULTADOS FINALES ---")
    for est in registro:
        nombre = est["nombre"]
        nota   = est["nota"]

        # Determinamos el estado según la nota
        if nota >= 90:
            estado = "Excelente"
        elif nota >= 70:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"  {nombre}: {nota} puntos → {estado}")

    # Mostramos el promedio con 2 decimales usando :.2f
    promedio = calcular_promedio()
    print(f"\nPromedio del grupo: {promedio:.2f}")

# ✅ main() organiza y controla todo el flujo del programa
def main():
    print("\n=== Bienvenido al Sistema de Registro ===")

    # Pedimos cuántos estudiantes ingresar, con manejo de error
    try:
        cantidad = int(input("¿Cuántos estudiantes vas a registrar? "))
    except ValueError:
        print("Error: debes ingresar un número entero.")
        return  # Salimos de main si el dato es inválido

    # Registramos cada estudiante con un bucle
    for i in range(cantidad):
        nombre = input(f"\nNombre del estudiante {i + 1}: ")

        try:
            nota = float(input(f"Nota de {nombre} (0 a 100): "))
        except ValueError:
            print("Nota inválida. Se asignará 0 automáticamente.")
            nota = 0

        registrar_estudiante(nombre, nota)

    # Al terminar, mostramos todos los resultados
    mostrar_resultados()

# ✅ Punto de entrada del programa
main()
