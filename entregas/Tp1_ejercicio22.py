# Ejercicio 22 - Guía de Recursividad
# El problema de la mochila Jedi.
#
# Un Jedi está atrapado y su mochila (representada como una lista) contiene varios objetos.
# Implementar la función recursiva "usar_la_fuerza" que:
#   a) Saque los objetos de a uno hasta encontrar un sable de luz o quedarse sin objetos.
#   b) Determine si la mochila contiene un sable de luz y cuántos objetos fueron necesarios
#      sacar para encontrarlo.
#   c) Utiliza una lista para representar la mochila.

SABLE_DE_LUZ = "sable de luz"

def usar_la_fuerza(mochila: list, objetos_sacados: int = 0) -> tuple:
    """
    Busca un sable de luz en la mochila de forma recursiva,
    sacando objetos de a uno desde el principio de la lista.

    Caso base 1: la mochila está vacía → no se encontró el sable.
    Caso base 2: el primer objeto es el sable de luz → se encontró.
    Caso recursivo: el primer objeto no es el sable → se saca (se descarta)
                    y se llama recursivamente con el resto de la mochila.

    Parámetros:
        mochila (list)         : lista de objetos que contiene la mochila.
        objetos_sacados (int)  : contador acumulado de objetos sacados (parámetro interno).

    Retorna:
        tuple: (encontrado: bool, cantidad_sacados: int)
            - encontrado      : True si se encontró el sable, False si no.
            - cantidad_sacados: cuántos objetos se sacaron para encontrarlo
                                (o el total si no se encontró).
    """
    # Caso base: mochila vacía, no había sable de luz
    if len(mochila) == 0:
        return (False, objetos_sacados)

    objeto_actual = mochila[0]
    print(f"  Sacando objeto #{objetos_sacados + 1}: '{objeto_actual}'")

    # Caso base: encontramos el sable de luz
    if objeto_actual == SABLE_DE_LUZ:
        return (True, objetos_sacados + 1)

    # Caso recursivo: no es el sable, seguir buscando en el resto
    return usar_la_fuerza(mochila[1:], objetos_sacados + 1)


# ── Pruebas ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    def mostrar_resultado(descripcion: str, mochila: list) -> None:
        print(f"\n{'=' * 50}")
        print(f"Jedi: {descripcion}")
        print(f"Mochila: {mochila}")
        print("Usando la fuerza...")
        encontrado, cantidad = usar_la_fuerza(mochila)
        print(f"\nResultado:")
        if encontrado:
            print(f"  ✓ ¡Sable de luz encontrado! Se sacaron {cantidad} objeto(s).")
        else:
            print(f"  ✗ No había sable de luz. Se vaciaron los {cantidad} objeto(s).")

    # Caso 1: sable al final
    mostrar_resultado(
        "Luke Skywalker",
        ["cantimplora", "raciones", "comlink", "capa", SABLE_DE_LUZ]
    )

    # Caso 2: sable al principio
    mostrar_resultado(
        "Obi-Wan Kenobi",
        [SABLE_DE_LUZ, "mapa estelar", "bata"]
    )

    # Caso 3: sin sable de luz
    mostrar_resultado(
        "Rey (mochila sin sable)",
        ["bastón", "raciones", "cuerdas", "linterna"]
    )

    # Caso 4: mochila vacía
    mostrar_resultado(
        "Rey (mochila vacía)",
        []
    )