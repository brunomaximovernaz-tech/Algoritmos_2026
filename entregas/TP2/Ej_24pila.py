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


# ── Funciones auxiliares ──────────────────────────────────────────────────────

def copiar_pila(pila):
    """Copia una pila usando una pila auxiliar para no perder los datos."""
    aux = Pila()
    copia = Pila()
    # Vaciar en auxiliar (invierte el orden)
    while not pila.esta_vacia():
        aux.apilar(pila.desapilar())
    # Restaurar original y llenar copia
    while not aux.esta_vacia():
        elemento = aux.desapilar()
        pila.apilar(elemento)
        copia.apilar(elemento)
    return copia


# ── Consultas ─────────────────────────────────────────────────────────────────

def posicion_personaje(pila, nombre):
    """
    a) Determina en qué posición se encuentra un personaje,
       tomando posición 1 como la cima de la pila.
    """
    aux = Pila()
    posicion = 1
    resultado = None

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento["nombre"].lower() == nombre.lower():
            resultado = posicion
        aux.apilar(elemento)
        posicion += 1

    # Restaurar pila original
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return resultado


def mas_de_cinco_peliculas(pila):
    """
    b) Retorna una lista con los personajes que participaron
       en más de 5 películas, junto con la cantidad.
    """
    aux = Pila()
    encontrados = []

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento["peliculas"] > 5:
            encontrados.append(elemento)
        aux.apilar(elemento)

    # Restaurar pila original
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return encontrados


def peliculas_viuda_negra(pila):
    """
    c) Retorna cuántas películas participó la Viuda Negra (Black Widow).
    """
    aux = Pila()
    resultado = None

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        nombre = elemento["nombre"].lower()
        if "viuda negra" in nombre or "black widow" in nombre or "natasha" in nombre:
            resultado = elemento["peliculas"]
        aux.apilar(elemento)

    # Restaurar pila original
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return resultado


def personajes_por_inicial(pila, iniciales):
    """
    d) Retorna una lista con todos los personajes cuyo nombre
       empieza con alguna de las letras indicadas.
    """
    aux = Pila()
    encontrados = []
    iniciales_upper = [i.upper() for i in iniciales]

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento["nombre"][0].upper() in iniciales_upper:
            encontrados.append(elemento)
        aux.apilar(elemento)

    # Restaurar pila original
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return encontrados


# ── Programa principal ────────────────────────────────────────────────────────

if __name__ == "__main__":

    # Carga de datos en la pila (fondo → cima)
    personajes_mcu = [
        {"nombre": "Iron Man",          "peliculas": 10},
        {"nombre": "Capitán América",   "peliculas": 5},
        {"nombre": "Thor",              "peliculas": 8},
        {"nombre": "Viuda Negra",       "peliculas": 7},
        {"nombre": "Hawkeye",           "peliculas": 6},
        {"nombre": "Hulk",              "peliculas": 7},
        {"nombre": "Doctor Strange",    "peliculas": 4},
        {"nombre": "Groot",             "peliculas": 5},
        {"nombre": "Guerra Infinita",   "peliculas": 1},
        {"nombre": "Gamora",            "peliculas": 4},
        {"nombre": "Rocket Raccoon",    "peliculas": 5},
        {"nombre": "Pantera Negra",     "peliculas": 3},
        {"nombre": "Wanda Maximoff",    "peliculas": 6},
        {"nombre": "Spider-Man",        "peliculas": 6},
        {"nombre": "Capitana Marvel",   "peliculas": 3},
    ]

    pila = Pila()
    for p in personajes_mcu:
        pila.apilar(p)

    print("=" * 55)
    print("       PILA DE PERSONAJES MCU")
    print("=" * 55)

    # a) Posición de Rocket Raccoon y Groot
    print("\na) Posición desde la cima:")
    for nombre in ["Rocket Raccoon", "Groot"]:
        pos = posicion_personaje(pila, nombre)
        if pos:
            print(f"   {nombre}: posición {pos}")
        else:
            print(f"   {nombre}: no encontrado en la pila")

    # b) Personajes con más de 5 películas
    print("\nb) Personajes con más de 5 películas:")
    lista = mas_de_cinco_peliculas(pila)
    if lista:
        for p in lista:
            print(f"   {p['nombre']}: {p['peliculas']} películas")
    else:
        print("   Ninguno.")

    # c) Películas de Viuda Negra
    print("\nc) Películas de la Viuda Negra:")
    cant = peliculas_viuda_negra(pila)
    if cant is not None:
        print(f"   Participó en {cant} películas.")
    else:
        print("   No se encontró a la Viuda Negra en la pila.")

    # d) Personajes que empiezan con C, D y G
    print("\nd) Personajes cuyo nombre empieza con C, D o G:")
    lista_cdg = personajes_por_inicial(pila, ["C", "D", "G"])
    if lista_cdg:
        for p in lista_cdg:
            print(f"   {p['nombre']} ({p['peliculas']} películas)")
    else:
        print("   Ninguno.")

    print("\n" + "=" * 55)
