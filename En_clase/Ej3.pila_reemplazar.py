"""
Reemplazar todas las ocurrencias de un determinado elemento en una pila (Stack).

La pila se representa con una lista de Python donde:
  - El tope (top) es el último elemento: pila[-1]
  - push  -> pila.append(elemento)
  - pop   -> pila.pop()
  - peek  -> pila[-1]
  - vacía -> len(pila) == 0

Estrategia:
  1. Sacar cada elemento de la pila original.
  2. Si coincide con el buscado, apilarlo ya reemplazado; si no, tal cual.
  Para mantener el orden original se usa una pila auxiliar.
"""

# ─────────────────────────────────────────────
# Enfoque ITERATIVO
# ─────────────────────────────────────────────

def reemplazar_iterativo(pila: list, viejo, nuevo) -> list:
    """
    Reemplaza todas las ocurrencias de 'viejo' por 'nuevo' en la pila.
    Preserva el orden original de los elementos.
    No modifica la pila original; devuelve una nueva.
    """
    auxiliar = []

    # Paso 1: vaciar la pila original en la auxiliar
    #         (los elementos quedan en orden invertido en auxiliar)
    temp = list(pila)           # copia para no destruir la original
    while temp:
        elemento = temp.pop()
        auxiliar.append(elemento)

    # Paso 2: reconstruir la pila resultado aplicando el reemplazo
    resultado = []
    while auxiliar:
        elemento = auxiliar.pop()
        if elemento == viejo:
            resultado.append(nuevo) 
        else:
            resultado.append(elemento)

    return resultado


# ─────────────────────────────────────────────
# Enfoque RECURSIVO
# ─────────────────────────────────────────────

def reemplazar_recursivo(pila: list, viejo, nuevo) -> list:
    """
    Versión recursiva.
    Caso base  : pila vacía -> devuelve lista vacía.
    Paso recur.: toma el tope, decide si reemplaza, y llama al resto.
    """
    if not pila:                            # caso base
        return []

    tope = pila[-1]                         # peek
    resto = pila[:-1]                       # sub-pila sin el tope

    elemento_nuevo = nuevo if tope == viejo else tope

    return reemplazar_recursivo(resto, viejo, nuevo) + [elemento_nuevo]


# ─────────────────────────────────────────────
# Pruebas
# ─────────────────────────────────────────────

if __name__ == "__main__":

    # Pila de ejemplo  (tope → derecha)
    #  fondo [1, 2, 3, 2, 4, 2, 5] tope
    pila_original = [1, 2, 3, 2, 4, 2, 5]

    print("Pila original:     ", pila_original)

    # ── Iterativo ──
    resultado_iter = reemplazar_iterativo(pila_original, viejo=2, nuevo=99)
    print("Iterativo  (2->99):", resultado_iter)

    # -- Recursivo --
    resultado_rec = reemplazar_recursivo(pila_original, viejo=2, nuevo=99)
    print("Recursivo  (2->99):", resultado_rec)

    # -- Caso sin ocurrencias --
    sin_ocurrencias = reemplazar_iterativo(pila_original, viejo=7, nuevo=99)
    print("Sin ocurrencias:   ", sin_ocurrencias)

    # -- Pila con strings --
    pila_str = ["a", "b", "a", "c", "a"]
    print("\nPila strings:      ", pila_str)
    print("Iter  ('a'->'X'):  ", reemplazar_iterativo(pila_str, "a", "X"))
    print("Recur ('a'->'X'):  ", reemplazar_recursivo(pila_str, "a", "X"))

    # ── Pila vacía ──
    print("\nPila vacía:        ", reemplazar_iterativo([], 1, 9))
