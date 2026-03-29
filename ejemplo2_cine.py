# ============================================================
# EJEMPLO 2: SISTEMA DE CINE
# Temas: variables, listas, diccionarios, funciones, lambdas,
#        bucles, condicionales, operadores, manejo de errores
# ============================================================

# ── Configuración del cine (cambia estos valores para ajustar el tamaño) ──
FILAS      = 5       # int: número de filas
COLUMNAS   = 8       # int: número de columnas por fila
PRECIO     = 18000   # int: precio por tiquete en COP

# ── Símbolos visuales ─────────────────────────────────────────────────────
LIBRE    = "[ ]"
OCUPADO  = "[X]"

# ── Lambda: generar clave de asiento (ej: fila 2, col 3 → "2-3") ─────────
clave_asiento = lambda fila, columna: f"{fila}-{columna}"

# ── Lambda: capacidad total ───────────────────────────────────────────────
capacidad_total = lambda: FILAS * COLUMNAS


# ════════════════════════════════════════════════════════════
# FUNCIONES DE VALIDACIÓN
# ════════════════════════════════════════════════════════════

def pedir_entero(mensaje, minimo=1, maximo=None):
    """Pide un entero al usuario con validación de rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"  ⚠ El valor mínimo es {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ⚠ El valor máximo es {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ✗ Ingresa un número entero válido.")


def pedir_texto(mensaje):
    """Pide un texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  ✗ El campo no puede estar vacío.")


# ════════════════════════════════════════════════════════════
# FUNCIONES DEL CINE
# ════════════════════════════════════════════════════════════

def crear_sala():
    """
    Crea la sala de cine como un diccionario de asientos.
    Clave: "fila-columna" (str) → Valor: True (libre) o False (ocupado)
    Usa bucles for anidados para recorrer filas y columnas.
    """
    sala = {}
    for fila in range(1, FILAS + 1):
        for col in range(1, COLUMNAS + 1):
            sala[clave_asiento(fila, col)] = True   # True = libre
    return sala


def mostrar_sala(sala):
    """
    Muestra la sala con filas y columnas.
    [ ] = libre   [X] = ocupado
    Usa bucles for anidados para reconstruir la grilla.
    """
    ocupados = sum(1 for v in sala.values() if not v)   # Contar ocupados
    libres   = capacidad_total() - ocupados

    print(f"\n  Sala: {FILAS} filas × {COLUMNAS} columnas | "
          f"Capacidad: {capacidad_total()} | Libres: {libres} | Ocupados: {ocupados}")

    # Encabezado de columnas
    encabezado = "       " + "  ".join(f"C{c:<2}" for c in range(1, COLUMNAS + 1))
    print(f"\n{encabezado}")
    print("       " + "─" * (COLUMNAS * 5))

    # Fila por fila
    for fila in range(1, FILAS + 1):
        fila_str = f"  F{fila:<3} |"
        for col in range(1, COLUMNAS + 1):
            clave = clave_asiento(fila, col)
            simbolo = LIBRE if sala[clave] else OCUPADO
            fila_str += f" {simbolo}"
        print(fila_str)

    print()


def comprar_tiquete(sala):
    """
    El usuario elige fila y columna para comprar un tiquete.
    Valida que el asiento exista y esté libre.
    """
    print(f"\n  ── Comprar tiquete (precio: ${PRECIO:,}) ──")
    mostrar_sala(sala)

    fila = pedir_entero(f"  Fila (1 a {FILAS}): ", minimo=1, maximo=FILAS)
    col  = pedir_entero(f"  Columna (1 a {COLUMNAS}): ", minimo=1, maximo=COLUMNAS)

    clave = clave_asiento(fila, col)

    if not sala[clave]:
        print(f"  ✗ El asiento F{fila}-C{col} ya está ocupado. Elige otro.")
        return

    nombre = pedir_texto("  Nombre del comprador: ")

    # Confirmar compra
    confirmacion = input(f"  ¿Confirmar tiquete F{fila}-C{col} para {nombre}? (s/n): ").strip().lower()
    if confirmacion == "s":
        sala[clave] = False   # Marcar como ocupado (False)
        print(f"  ✔ Tiquete vendido. Asiento F{fila}-C{col} | ${PRECIO:,} COP")
    else:
        print("  Compra cancelada.")


def cancelar_tiquete(sala):
    """
    Libera un asiento previamente ocupado.
    Valida que el asiento exista y esté realmente ocupado.
    """
    print(f"\n  ── Cancelar tiquete ──")
    mostrar_sala(sala)

    fila = pedir_entero(f"  Fila (1 a {FILAS}): ", minimo=1, maximo=FILAS)
    col  = pedir_entero(f"  Columna (1 a {COLUMNAS}): ", minimo=1, maximo=COLUMNAS)

    clave = clave_asiento(fila, col)

    if sala[clave]:
        print(f"  ✗ El asiento F{fila}-C{col} ya está libre.")
        return

    confirmacion = input(f"  ¿Cancelar y liberar el asiento F{fila}-C{col}? (s/n): ").strip().lower()
    if confirmacion == "s":
        sala[clave] = True    # Volver a marcar como libre
        print(f"  ✔ Asiento F{fila}-C{col} liberado.")
    else:
        print("  Cancelación abortada.")


def resumen_ventas(sala):
    """
    Muestra el resumen de ocupación y las ganancias estimadas.
    Usa operadores aritméticos y bucles.
    """
    ocupados = sum(1 for v in sala.values() if not v)
    libres   = capacidad_total() - ocupados
    ganancias = ocupados * PRECIO
    porcentaje = round((ocupados / capacidad_total()) * 100, 1)

    print(f"""
  ╔══════════════════════════════════════╗
  ║          RESUMEN DE LA SALA          ║
  ╠══════════════════════════════════════╣
  ║  Capacidad total: {capacidad_total():<20}║
  ║  Asientos ocupados: {ocupados:<18}║
  ║  Asientos libres:   {libres:<18}║
  ║  Ocupación:         {porcentaje}%{'':<16}║
  ║  Ganancias:         ${ganancias:<17,}║
  ╚══════════════════════════════════════╝""")

    # Mostrar cuáles filas tienen asientos libres usando continue
    print("  Asientos libres por fila:")
    for fila in range(1, FILAS + 1):
        libres_fila = [
            f"C{col}" for col in range(1, COLUMNAS + 1)
            if sala[clave_asiento(fila, col)]
        ]
        if not libres_fila:
            print(f"    F{fila}: COMPLETA")
            continue                         # ← continue: salta al siguiente fila
        print(f"    F{fila}: {', '.join(libres_fila)}")


# ════════════════════════════════════════════════════════════
# MENÚ PRINCIPAL
# ════════════════════════════════════════════════════════════

def main():
    sala = crear_sala()
    print(f"\n  🎬 Bienvenido al Cine — Sala de {FILAS}×{COLUMNAS} ({capacidad_total()} asientos)")

    while True:
        print("""
  ╔══════════════════════════════════╗
  ║         SISTEMA DE CINE          ║
  ╠══════════════════════════════════╣
  ║  1. Ver sala                     ║
  ║  2. Comprar tiquete              ║
  ║  3. Cancelar tiquete             ║
  ║  4. Resumen de ventas            ║
  ║  0. Salir                        ║
  ╚══════════════════════════════════╝""")

        opcion = pedir_entero("  Opción: ", minimo=0, maximo=4)

        if opcion == 0:
            print("\n  ¡Hasta luego! 🎬\n")
            break
        elif opcion == 1:
            mostrar_sala(sala)
        elif opcion == 2:
            # Verificar si la sala está llena antes de intentar vender
            if all(not v for v in sala.values()):   # all() con generador
                print("\n  ✗ La sala está completamente llena. No hay asientos disponibles.")
            else:
                comprar_tiquete(sala)
        elif opcion == 3:
            cancelar_tiquete(sala)
        elif opcion == 4:
            resumen_ventas(sala)


if __name__ == "__main__":
    main()
