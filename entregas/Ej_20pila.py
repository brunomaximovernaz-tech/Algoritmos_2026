DIRECCIONES = ["norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste", "suroeste"]

# Dirección opuesta para cada dirección (para volver al origen)
OPUESTOS = {
    "norte":    "sur",
    "sur":      "norte",
    "este":     "oeste",
    "oeste":    "este",
    "noreste":  "suroeste",
    "suroeste": "noreste",
    "noroeste": "sureste",
    "sureste":  "noroeste",
}


# ── Estructura Pila ───────────────────────────────────────────────────────────

class Pila:
    def __init__(self):
        self.__datos = []

    def apilar(self, elemento):
        self.__datos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.__datos.pop()

    def cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.__datos[-1]

    def esta_vacia(self):
        return len(self.__datos) == 0

    def __len__(self):
        return len(self.__datos)


# ── Algoritmo 1: Registrar movimientos ───────────────────────────────────────

def registrar_movimientos():
    """
    Solicita al usuario que ingrese movimientos del robot (dirección y pasos)
    y los apila. Retorna la pila con todos los movimientos registrados.
    """
    pila = Pila()
    print("=== Registro de movimientos del robot ===")
    print(f"Direcciones válidas: {', '.join(DIRECCIONES)}")
    print("Escriba 'fin' para terminar el registro.\n")

    while True:
        direccion = input("Dirección: ").strip().lower()
        if direccion == "fin":
            break
        if direccion not in DIRECCIONES:
            print(f"  ✗ Dirección inválida. Opciones: {', '.join(DIRECCIONES)}")
            continue
        try:
            pasos = int(input("Pasos: ").strip())
            if pasos <= 0:
                print("  ✗ Los pasos deben ser un número positivo.")
                continue
        except ValueError:
            print("  ✗ Ingrese un número entero para los pasos.")
            continue

        movimiento = {"direccion": direccion, "pasos": pasos}
        pila.apilar(movimiento)
        print(f"  ✓ Movimiento registrado: {pasos} paso(s) hacia el {direccion}\n")

    return pila


# ── Algoritmo 2: Generar secuencia de regreso ─────────────────────────────────

def generar_regreso(pila_movimientos):
    """
    Desapila los movimientos en orden inverso y genera la secuencia
    de movimientos opuestos para volver al punto de partida.

    El robot recorre el mismo camino al revés:
      - la dirección se invierte (norte → sur, noreste → suroeste, etc.)
      - la cantidad de pasos es la misma
    """
    print("\n=== Secuencia de regreso al punto de partida ===")

    if pila_movimientos.esta_vacia():
        print("No hay movimientos registrados.")
        return

    paso_num = 1
    while not pila_movimientos.esta_vacia():
        movimiento = pila_movimientos.desapilar()
        direccion_regreso = OPUESTOS[movimiento["direccion"]]
        print(f"  {paso_num}. {movimiento['pasos']} paso(s) hacia el {direccion_regreso}"
              f"  (invierte: {movimiento['direccion']})")
        paso_num += 1

    print("\n¡El robot volvió al punto de partida!")


# ── Programa principal ────────────────────────────────────────────────────────

if __name__ == "__main__":
    pila = registrar_movimientos()

    if pila.esta_vacia():
        print("No se registraron movimientos.")
    else:
        print(f"\nTotal de movimientos registrados: {len(pila)}")
        generar_regreso(pila)
