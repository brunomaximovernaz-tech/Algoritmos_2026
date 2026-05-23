from entero import Entero


class Main:
    @staticmethod
    def run():
        # ── Ingreso de dato ─────────────────────────────────────
        numero = int(input("Ingrese un número entero no negativo: "))
        entero = Entero(numero)

        # ── Resultados ──────────────────────────────────────────
        print()
        print(f"  Número    : {entero.get_numero()}")
        print(f"  Cuadrado  : {entero.cuadrado()}")
        print(f"  ¿Es par?   : {entero.es_par()}")
        print(f"  ¿Es impar? : {entero.es_impar()}")
        print(f"  Factorial : {entero.factorial()}")
        print(f"  ¿Es primo? : {entero.es_primo()}")

        # ── Prueba del setter ────────────────────────────────────
        print()
        nuevo = int(input("Ingrese otro número para modificar el objeto: "))
        entero.set_numero(nuevo)

        print()
        print(f"  Número    : {entero.get_numero()}")
        print(f"  Cuadrado  : {entero.cuadrado()}")
        print(f"  ¿Es par?   : {entero.es_par()}")
        print(f"  ¿Es impar? : {entero.es_impar()}")
        print(f"  Factorial : {entero.factorial()}")
        print(f"  ¿Es primo? : {entero.es_primo()}")


if __name__ == "__main__":
    Main.run()
