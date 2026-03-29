# ============================================================
# EJEMPLO 3: SISTEMA DE PARQUEADERO CON PERSISTENCIA
# Temas: variables, listas, diccionarios, funciones, lambdas,
#        bucles, condicionales, operadores, try/except, JSON
# ============================================================

import json
import os
from datetime import datetime

# ── Configuración del parqueadero ─────────────────────────
CAPACIDAD    = 10                     # int: máximo de vehículos
ARCHIVO_JSON = "parqueadero.json"     # str: archivo de persistencia

# ── Lambda: verificar si una placa tiene formato válido ───
# Una placa colombiana tiene 6 caracteres: 3 letras + 3 números (ej: ABC123)
placa_valida = lambda p: (
    len(p) == 6 and
    p[:3].isalpha() and
    p[3:].isdigit()
)

# ── Lambda: plazas disponibles ────────────────────────────
plazas_disponibles = lambda plazas: sum(1 for p in plazas if p is None)


# ════════════════════════════════════════════════════════════
# FUNCIONES DE PERSISTENCIA (JSON)
# ════════════════════════════════════════════════════════════

def guardar_estado(plazas):
    """
    Guarda el estado actual del parqueadero en un archivo JSON.
    Convierte None a null (JSON) automáticamente.
    """
    datos = {
        "capacidad": CAPACIDAD,
        "plazas": plazas           # Lista: None si libre, dict si ocupado
    }
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)


def cargar_estado():
    """
    Carga el estado desde el archivo JSON.
    Si no existe o está dañado, crea un parqueadero vacío.
    Usa try/except para manejar errores de lectura.
    """
    if not os.path.exists(ARCHIVO_JSON):
        # Primera vez: crear lista de CAPACIDAD plazas vacías (None)
        return [None] * CAPACIDAD

    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        plazas = datos.get("plazas", [])

        # Verificar que tenga la capacidad correcta
        if len(plazas) != CAPACIDAD:
            print("  ⚠ El archivo no coincide con la capacidad actual. Reiniciando.")
            return [None] * CAPACIDAD

        return plazas

    except (json.JSONDecodeError, KeyError):
        print("  ⚠ Archivo de datos dañado. Iniciando parqueadero vacío.")
        return [None] * CAPACIDAD


# ════════════════════════════════════════════════════════════
# FUNCIONES DE VALIDACIÓN
# ════════════════════════════════════════════════════════════

def pedir_placa():
    """
    Pide una placa al usuario.
    Valida formato colombiano: 3 letras + 3 números (ej: ABC123).
    """
    while True:
        placa = input("  Placa del vehículo (ej: ABC123): ").strip().upper()
        if not placa:
            print("  ✗ La placa no puede estar vacía.")
        elif not placa_valida(placa):
            print("  ✗ Formato inválido. Debe ser 3 letras + 3 números (ej: ABC123).")
        else:
            return placa


def pedir_entero(mensaje, minimo=0, maximo=None):
    """Pide un entero al usuario con validación."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"  ⚠ Mínimo permitido: {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ⚠ Máximo permitido: {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ✗ Ingresa un número entero.")


# ════════════════════════════════════════════════════════════
# FUNCIONES DEL PARQUEADERO
# ════════════════════════════════════════════════════════════

def mostrar_estado(plazas):
    """
    Muestra el estado completo del parqueadero.
    Lista todas las plazas: vacías y ocupadas.
    Siempre muestra cuántas hay disponibles.
    """
    disponibles = plazas_disponibles(plazas)
    ocupadas    = CAPACIDAD - disponibles

    print(f"\n  🅿 Parqueadero — {disponibles} libre(s) | {ocupadas} ocupada(s) | Capacidad: {CAPACIDAD}")
    print("  " + "─" * 55)
    print(f"  {'Plaza':<8} {'Estado':<12} {'Placa':<10} {'Entrada'}")
    print("  " + "─" * 55)

    for i, plaza in enumerate(plazas):
        num = i + 1                          # Las plazas se muestran desde 1
        if plaza is None:
            print(f"  {num:<8} {'LIBRE':<12} {'─':<10} {'─'}")
        else:
            print(f"  {num:<8} {'OCUPADA':<12} {plaza['placa']:<10} {plaza['entrada']}")

    print("  " + "─" * 55)

    # Resumen de placas activas con list comprehension
    placas_activas = [p["placa"] for p in plazas if p is not None]
    if placas_activas:
        print(f"  Vehículos en el sistema: {', '.join(placas_activas)}")
    else:
        print("  No hay vehículos en el parqueadero.")


def buscar_placa(plazas, placa):
    """
    Busca una placa en las plazas.
    Retorna el índice si la encuentra, o -1 si no.
    Aplica: for con enumerate, condicionales.
    """
    for i, plaza in enumerate(plazas):
        if plaza is not None and plaza["placa"] == placa:
            return i           # Retorna el índice donde está
    return -1                  # No encontrada


def ingresar_vehiculo(plazas):
    """
    Registra la entrada de un vehículo al parqueadero.
    Valida: capacidad, placa no duplicada, formato de placa.
    """
    print("\n  ── Ingreso de vehículo ──")

    # Verificar si hay plazas disponibles
    if plazas_disponibles(plazas) == 0:
        print("  ✗ El parqueadero está lleno. No hay plazas disponibles.")
        return

    placa = pedir_placa()

    # Verificar si la placa ya está dentro
    indice = buscar_placa(plazas, placa)
    if indice != -1:
        print(f"  ✗ La placa {placa} ya está registrada en la plaza {indice + 1}.")
        return

    # Buscar la primera plaza libre con un bucle for + break
    plaza_asignada = -1
    for i, plaza in enumerate(plazas):
        if plaza is None:
            plaza_asignada = i
            break                            # ← break: encontramos la primera libre

    # Registrar el vehículo con hora de entrada
    hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M")
    plazas[plaza_asignada] = {
        "placa":   placa,
        "entrada": hora_entrada,
    }

    guardar_estado(plazas)                   # Persistencia inmediata
    print(f"  ✔ {placa} ingresado en plaza {plaza_asignada + 1} a las {hora_entrada}.")
    print(f"  Plazas disponibles ahora: {plazas_disponibles(plazas)}")


def retirar_vehiculo(plazas):
    """
    Registra la salida de un vehículo del parqueadero.
    Libera la plaza y guarda el estado actualizado.
    """
    print("\n  ── Retiro de vehículo ──")

    # Verificar que haya vehículos adentro
    if plazas_disponibles(plazas) == CAPACIDAD:
        print("  ✗ El parqueadero está vacío. No hay vehículos para retirar.")
        return

    placa = pedir_placa()

    indice = buscar_placa(plazas, placa)

    if indice == -1:
        print(f"  ✗ La placa {placa} no está en el parqueadero.")
        return

    # Calcular tiempo de permanencia
    entrada_str = plazas[indice]["entrada"]
    try:
        entrada_dt  = datetime.strptime(entrada_str, "%Y-%m-%d %H:%M")
        ahora       = datetime.now()
        diferencia  = ahora - entrada_dt
        minutos     = int(diferencia.total_seconds() / 60)
        tiempo_str  = f"{minutos} minuto(s)"
    except Exception:
        tiempo_str = "desconocido"

    print(f"  Vehículo: {placa} | Plaza: {indice + 1} | Tiempo: {tiempo_str}")
    confirmacion = input("  ¿Confirmar retiro? (s/n): ").strip().lower()

    if confirmacion == "s":
        plazas[indice] = None               # Liberar la plaza → None
        guardar_estado(plazas)              # Guardar estado actualizado
        print(f"  ✔ {placa} retirado. Plaza {indice + 1} libre.")
        print(f"  Plazas disponibles ahora: {plazas_disponibles(plazas)}")
    else:
        print("  Retiro cancelado.")


def consultar_placa(plazas):
    """
    Consulta si una placa específica está en el parqueadero.
    Informa en qué plaza y desde cuándo.
    """
    print("\n  ── Consultar placa ──")
    placa = pedir_placa()
    indice = buscar_placa(plazas, placa)

    if indice == -1:
        print(f"  ✗ La placa {placa} NO está en el parqueadero.")
    else:
        print(f"  ✔ La placa {placa} SÍ está en el parqueadero.")
        print(f"     Plaza:   {indice + 1}")
        print(f"     Entrada: {plazas[indice]['entrada']}")


# ════════════════════════════════════════════════════════════
# MENÚ PRINCIPAL
# ════════════════════════════════════════════════════════════

def main():
    # Cargar estado guardado (o crear vacío si es la primera vez)
    plazas = cargar_estado()
    ocupadas_al_inicio = CAPACIDAD - plazas_disponibles(plazas)
    print(f"\n  🅿 Parqueadero iniciado — {ocupadas_al_inicio} vehículo(s) cargado(s) desde '{ARCHIVO_JSON}'.")

    while True:
        # Siempre mostrar disponibilidad en el menú
        disponibles = plazas_disponibles(plazas)
        print(f"""
  ╔══════════════════════════════════════╗
  ║         SISTEMA DE PARQUEADERO       ║
  ║     Plazas disponibles: {disponibles:<3} / {CAPACIDAD:<3}      ║
  ╠══════════════════════════════════════╣
  ║  1. Ver estado del parqueadero       ║
  ║  2. Ingresar vehículo                ║
  ║  3. Retirar vehículo                 ║
  ║  4. Consultar placa                  ║
  ║  0. Salir                            ║
  ╚══════════════════════════════════════╝""")

        opcion = pedir_entero("  Opción: ", minimo=0, maximo=4)

        if opcion == 0:
            print("\n  ¡Hasta luego! 🅿\n")
            break
        elif opcion == 1:
            mostrar_estado(plazas)
        elif opcion == 2:
            ingresar_vehiculo(plazas)
        elif opcion == 3:
            retirar_vehiculo(plazas)
        elif opcion == 4:
            consultar_placa(plazas)


if __name__ == "__main__":
    main()
