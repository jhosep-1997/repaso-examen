# ============================================================
# EJEMPLO 1: SISTEMA DE ESTUDIANTES CON ARCHIVO CSV
# Temas: variables, tipos, listas, diccionarios, funciones,
#        lambdas, bucles, condicionales, errores, CSV, split()
# ============================================================

import csv
import os

# ── Constantes ──────────────────────────────────────────────
ARCHIVO_CSV = "estudiantes.csv"
NOTA_MIN    = 0.0
NOTA_MAX    = 5.0
NUM_NOTAS   = 3

# ── Lambda: calcular promedio de una lista de notas ─────────
calcular_promedio = lambda notas: round(sum(notas) / len(notas), 2)

# ── Lambda: estado según promedio ───────────────────────────
estado = lambda promedio: "Aprobado ✔" if promedio >= 3.0 else "Reprobado ✘"


# ════════════════════════════════════════════════════════════
# FUNCIONES DE VALIDACIÓN (manejo de errores con try/except)
# ════════════════════════════════════════════════════════════

def pedir_texto(mensaje):
    """Pide un texto no vacío al usuario."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  ✗ El campo no puede estar vacío.")


def pedir_nota(mensaje):
    """
    Pide una nota entre NOTA_MIN y NOTA_MAX.
    Usa try/except para capturar entradas no numéricas.
    """
    while True:
        try:
            nota = float(input(mensaje))
            if NOTA_MIN <= nota <= NOTA_MAX:
                return nota
            print(f"  ⚠ La nota debe estar entre {NOTA_MIN} y {NOTA_MAX}.")
        except ValueError:
            print("  ✗ Ingresa un número válido (ej: 3.5).")


def pedir_entero(mensaje, minimo=0, maximo=None):
    """Pide un número entero dentro de un rango opcional."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"  ⚠ Debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ⚠ Debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ✗ Ingresa un número entero.")


# ════════════════════════════════════════════════════════════
# FUNCIONES DE CSV
# ════════════════════════════════════════════════════════════

def guardar_csv(lista_estudiantes):
    """
    Guarda la lista de diccionarios en el archivo CSV.
    Escribe encabezado + una fila por estudiante.
    """
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        # Encabezado
        writer.writerow(["id", "nombre", "apellido", "nota1", "nota2", "nota3", "promedio"])
        for e in lista_estudiantes:
            writer.writerow([
                e["id"], e["nombre"], e["apellido"],
                e["nota1"], e["nota2"], e["nota3"], e["promedio"]
            ])


def cargar_csv():
    """
    Carga el CSV y retorna una lista de diccionarios.
    Si el archivo no existe, retorna lista vacía.
    Usa split() para separar nombre completo si es necesario.
    """
    estudiantes = []

    if not os.path.exists(ARCHIVO_CSV):
        return estudiantes                   # Archivo aún no existe → lista vacía

    with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
        contenido = archivo.read().strip()

        if not contenido:
            return estudiantes               # Archivo vacío → lista vacía

        lineas = contenido.split("\n")       # ← split() para separar líneas del CSV

        # La primera línea es el encabezado, la saltamos con [1:]
        for linea in lineas[1:]:
            if not linea.strip():
                continue

            # split(",") separa cada campo de la línea CSV
            partes = linea.split(",")

            # Verificar que la línea tenga exactamente 7 campos
            if len(partes) != 7:
                print(f"  ⚠ Línea con formato incorrecto ignorada: {linea}")
                continue

            try:
                estudiantes.append({
                    "id":       int(partes[0]),
                    "nombre":   partes[1].strip(),
                    "apellido": partes[2].strip(),
                    "nota1":    float(partes[3]),
                    "nota2":    float(partes[4]),
                    "nota3":    float(partes[5]),
                    "promedio": float(partes[6]),
                })
            except ValueError:
                print(f"  ⚠ No se pudo leer la línea: {linea}")

    return estudiantes


def siguiente_id(lista_estudiantes):
    """Genera el próximo ID basándose en el máximo actual."""
    if not lista_estudiantes:
        return 1
    return max(e["id"] for e in lista_estudiantes) + 1


# ════════════════════════════════════════════════════════════
# FUNCIONES DE NEGOCIO
# ════════════════════════════════════════════════════════════

def agregar_estudiante(lista_estudiantes):
    """Pide datos al usuario y agrega un nuevo estudiante."""
    print("\n  ── Agregar estudiante ──")
    nombre   = pedir_texto("  Nombre:   ").capitalize()
    apellido = pedir_texto("  Apellido: ").capitalize()

    print(f"  Ingresa {NUM_NOTAS} notas (entre {NOTA_MIN} y {NOTA_MAX}):")
    notas = []
    for i in range(1, NUM_NOTAS + 1):
        nota = pedir_nota(f"    Nota {i}: ")
        notas.append(nota)

    promedio_calculado = calcular_promedio(notas)

    nuevo = {
        "id":       siguiente_id(lista_estudiantes),
        "nombre":   nombre,
        "apellido": apellido,
        "nota1":    notas[0],
        "nota2":    notas[1],
        "nota3":    notas[2],
        "promedio": promedio_calculado,
    }

    lista_estudiantes.append(nuevo)
    guardar_csv(lista_estudiantes)
    print(f"\n  ✔ {nombre} {apellido} agregado. Promedio: {promedio_calculado} — {estado(promedio_calculado)}")


def eliminar_estudiante(lista_estudiantes):
    """Elimina un estudiante por su ID."""
    if not lista_estudiantes:
        print("\n  ✗ No hay estudiantes registrados.")
        return

    ver_todos(lista_estudiantes)
    id_eliminar = pedir_entero("\n  ID del estudiante a eliminar: ", minimo=1)

    # Buscar el estudiante con ese ID
    encontrado = None
    for e in lista_estudiantes:
        if e["id"] == id_eliminar:
            encontrado = e
            break

    if encontrado is None:
        print(f"  ✗ No existe un estudiante con ID {id_eliminar}.")
        return

    confirmacion = input(f"  ¿Eliminar a {encontrado['nombre']} {encontrado['apellido']}? (s/n): ").strip().lower()
    if confirmacion == "s":
        lista_estudiantes.remove(encontrado)
        guardar_csv(lista_estudiantes)
        print("  ✔ Estudiante eliminado.")
    else:
        print("  Operación cancelada.")


def ver_todos(lista_estudiantes):
    """Muestra todos los estudiantes con sus promedios."""
    if not lista_estudiantes:
        print("\n  ✗ No hay estudiantes registrados.")
        return

    print(f"\n  {'ID':<5} {'Nombre':<15} {'Apellido':<15} {'N1':<6} {'N2':<6} {'N3':<6} {'Prom':<6} Estado")
    print("  " + "─" * 68)

    for e in lista_estudiantes:
        print(f"  {e['id']:<5} {e['nombre']:<15} {e['apellido']:<15} "
              f"{e['nota1']:<6} {e['nota2']:<6} {e['nota3']:<6} "
              f"{e['promedio']:<6} {estado(e['promedio'])}")

    # Promedio general del grupo usando lambda
    prom_general = calcular_promedio([e["promedio"] for e in lista_estudiantes])
    print(f"\n  Promedio general del grupo: {prom_general}")


def buscar_estudiante(lista_estudiantes):
    """Busca un estudiante por nombre o apellido."""
    if not lista_estudiantes:
        print("\n  ✗ No hay estudiantes registrados.")
        return

    termino = pedir_texto("  Buscar (nombre o apellido): ").lower()

    # Filtrar con list comprehension + operador 'in'
    resultados = [
        e for e in lista_estudiantes
        if termino in e["nombre"].lower() or termino in e["apellido"].lower()
    ]

    if not resultados:
        print(f"  ✗ No se encontraron resultados para '{termino}'.")
        return

    print(f"\n  Resultados para '{termino}':")
    for e in resultados:
        print(f"  → {e['nombre']} {e['apellido']} | "
              f"Notas: {e['nota1']}, {e['nota2']}, {e['nota3']} | "
              f"Promedio: {e['promedio']} | {estado(e['promedio'])}")


# ════════════════════════════════════════════════════════════
# MENÚ PRINCIPAL
# ════════════════════════════════════════════════════════════

def main():
    # Cargar datos existentes del CSV al iniciar
    estudiantes = cargar_csv()
    print(f"\n  Sistema de Estudiantes — {len(estudiantes)} registro(s) cargado(s) desde '{ARCHIVO_CSV}'.")

    while True:
        print("""
  ╔══════════════════════════════════╗
  ║     SISTEMA DE ESTUDIANTES       ║
  ╠══════════════════════════════════╣
  ║  1. Agregar estudiante           ║
  ║  2. Eliminar estudiante          ║
  ║  3. Ver todos los estudiantes    ║
  ║  4. Buscar estudiante            ║
  ║  0. Salir                        ║
  ╚══════════════════════════════════╝""")

        opcion = pedir_entero("  Opción: ", minimo=0, maximo=4)

        if opcion == 0:
            print("\n  ¡Hasta luego! 👋\n")
            break
        elif opcion == 1:
            agregar_estudiante(estudiantes)
        elif opcion == 2:
            eliminar_estudiante(estudiantes)
        elif opcion == 3:
            ver_todos(estudiantes)
        elif opcion == 4:
            buscar_estudiante(estudiantes)


if __name__ == "__main__":
    main()
