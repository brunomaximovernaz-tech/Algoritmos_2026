# Ejercicio 5 - Guía de Recursividad
# Desarrollar una función que permita convertir un número romano a un número decimal.

VALORES_ROMANOS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romano_a_decimal(romano: str) -> int:
    """
    Convierte un número romano a su equivalente decimal de forma recursiva.

    Caso base: si la cadena tiene un solo carácter, retorna su valor directamente.

    Caso recursivo: compara el valor del primer símbolo con el segundo.
      - Si el primero es MENOR que el segundo (ej. IV), se resta el primero
        y se suma el resultado del resto (sustracción romana).
      - Si el primero es MAYOR O IGUAL al segundo, se suma el primero
        y se continúa con el resto de la cadena.

    Parámetros:
        romano (str): cadena con el número romano a convertir (ej. "XIV").

    Retorna:
        int: el valor decimal equivalente.
    """
    # Caso base: un solo símbolo
    if len(romano) == 1:
        return VALORES_ROMANOS[romano]

    valor_actual = VALORES_ROMANOS[romano[0]]
    valor_siguiente = VALORES_ROMANOS[romano[1]]

    # Si el símbolo actual es menor que el siguiente, se resta (ej: IV = -1 + 5)
    if valor_actual < valor_siguiente:
        return -valor_actual + romano_a_decimal(romano[1:])
    else:
        return valor_actual + romano_a_decimal(romano[1:])


# ── Pruebas ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    casos = [
        ("I",      1),
        ("IV",     4),
        ("IX",     9),
        ("XIV",   14),
        ("XL",    40),
        ("XLII",  42),
        ("XCIX",  99),
        ("CDXLIV", 444),
        ("MCMXCIX", 1999),
        ("MMXXIV", 2024),
    ]

    print("Número Romano → Decimal")
    print("-" * 30)
    for romano, esperado in casos:
        resultado = romano_a_decimal(romano)
        estado = "✓" if resultado == esperado else f"✗ (esperado {esperado})"
        print(f"  {romano:>10}  →  {resultado:>5}  {estado}")