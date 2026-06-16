# Ejercicio 22 - Guía de Cola
# Cola con personajes del Marvel Cinematic Universe (MCU).
# Cada elemento tiene: nombre del personaje, nombre del superhéroe y género (M/F).
# Resolver:
#   a) Determinar el nombre del personaje de la superhéroe Capitana Marvel
#   b) Mostrar los nombres de los superhéroes femeninos
#   c) Mostrar los nombres de los personajes masculinos
#   d) Determinar el nombre del superhéroe del personaje Scott Lang
#   e) Mostrar todos los datos de superhéroes/personajes cuyos nombres comienzan con S
#   f) Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su superhéroe


# ── TDA Cola ─────────────────────────────────────────────────────────────────

class NodoCola:
    def __init__(self, info):
        self.info = info
        self.siguiente = None


class Cola:
    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamanio = 0

    def arribo(self, elemento):
        nuevo = NodoCola(elemento)
        if self.__final is None:
            self.__frente = nuevo
        else:
            self.__final.siguiente = nuevo
        self.__final = nuevo
        self.__tamanio += 1

    def atencion(self):
        if self.cola_vacia():
            raise IndexError("La cola está vacía")
        dato = self.__frente.info
        self.__frente = self.__frente.siguiente
        if self.__frente is None:
            self.__final = None
        self.__tamanio -= 1
        return dato

    def en_frente(self):
        if self.cola_vacia():
            raise IndexError("La cola está vacía")
        return self.__frente.info

    def cola_vacia(self):
        return self.__tamanio == 0

    def tamanio(self):
        return self.__tamanio


# ── Función auxiliar: recorrer sin perder datos ───────────────────────────────

def recorrer_cola(cola):
    """Devuelve una lista con todos los elementos y restaura la cola."""
    aux = Cola()
    elementos = []
    while not cola.cola_vacia():
        elem = cola.atencion()
        elementos.append(elem)
        aux.arribo(elem)
    while not aux.cola_vacia():
        cola.arribo(aux.atencion())
    return elementos


# ── Consultas ─────────────────────────────────────────────────────────────────

def a_personaje_capitana_marvel(cola):
    """a) Nombre del personaje cuyo superhéroe es Capitana Marvel."""
    for elem in recorrer_cola(cola):
        if elem["superheroe"].lower() == "capitana marvel":
            return elem["personaje"]
    return None


def b_superheroes_femeninos(cola):
    """b) Nombres de los superhéroes femeninos (género F)."""
    return [e["superheroe"] for e in recorrer_cola(cola) if e["genero"] == "F"]


def c_personajes_masculinos(cola):
    """c) Nombres de los personajes masculinos (género M)."""
    return [e["personaje"] for e in recorrer_cola(cola) if e["genero"] == "M"]


def d_superheroe_scott_lang(cola):
    """d) Nombre del superhéroe del personaje Scott Lang."""
    for elem in recorrer_cola(cola):
        if elem["personaje"].lower() == "scott lang":
            return elem["superheroe"]
    return None


def e_comienzan_con_s(cola):
    """e) Todos los datos de personajes o superhéroes cuyos nombres comienzan con S."""
    resultado = []
    for elem in recorrer_cola(cola):
        if elem["personaje"][0].upper() == "S" or elem["superheroe"][0].upper() == "S":
            resultado.append(elem)
    return resultado


def f_buscar_carol_danvers(cola):
    """f) Determina si Carol Danvers está en la cola e indica su superhéroe."""
    for elem in recorrer_cola(cola):
        if elem["personaje"].lower() == "carol danvers":
            return (True, elem["superheroe"])
    return (False, None)


# ── Programa principal ────────────────────────────────────────────────────────

if __name__ == "__main__":

    personajes_mcu = [
        {"personaje": "Tony Stark",        "superheroe": "Iron Man",         "genero": "M"},
        {"personaje": "Steve Rogers",      "superheroe": "Capitán América",  "genero": "M"},
        {"personaje": "Natasha Romanoff",  "superheroe": "Black Widow",      "genero": "F"},
        {"personaje": "Thor Odinson",      "superheroe": "Thor",             "genero": "M"},
        {"personaje": "Bruce Banner",      "superheroe": "Hulk",             "genero": "M"},
        {"personaje": "Clint Barton",      "superheroe": "Hawkeye",          "genero": "M"},
        {"personaje": "Carol Danvers",     "superheroe": "Capitana Marvel",  "genero": "F"},
        {"personaje": "Scott Lang",        "superheroe": "Ant-Man",          "genero": "M"},
        {"personaje": "Wanda Maximoff",    "superheroe": "Bruja Escarlata",  "genero": "F"},
        {"personaje": "Sam Wilson",        "superheroe": "Falcon",           "genero": "M"},
        {"personaje": "Peter Parker",      "superheroe": "Spider-Man",       "genero": "M"},
        {"personaje": "Shuri",             "superheroe": "Pantera Negra",    "genero": "F"},
        {"personaje": "Stephen Strange",   "superheroe": "Doctor Strange",   "genero": "M"},
        {"personaje": "Hope van Dyne",     "superheroe": "La Avispa",        "genero": "F"},
        {"personaje": "James Rhodes",      "superheroe": "War Machine",      "genero": "M"},
    ]

    cola = Cola()
    for p in personajes_mcu:
        cola.arribo(p)

    print("=" * 55)
    print("     COLA DE PERSONAJES MCU")
    print("=" * 55)

    # a)
    personaje = a_personaje_capitana_marvel(cola)
    print(f"\na) Personaje de Capitana Marvel: {personaje}")

    # b)
    femeninos = b_superheroes_femeninos(cola)
    print(f"\nb) Superhéroes femeninos ({len(femeninos)}):")
    for s in femeninos:
        print(f"   - {s}")

    # c)
    masculinos = c_personajes_masculinos(cola)
    print(f"\nc) Personajes masculinos ({len(masculinos)}):")
    for p in masculinos:
        print(f"   - {p}")

    # d)
    superheroe = d_superheroe_scott_lang(cola)
    print(f"\nd) Superhéroe de Scott Lang: {superheroe}")

    # e)
    con_s = e_comienzan_con_s(cola)
    print(f"\ne) Personajes/superhéroes que comienzan con S ({len(con_s)}):")
    for elem in con_s:
        print(f"   - {elem['personaje']} / {elem['superheroe']} ({elem['genero']})")

    # f)
    encontrado, superheroe_carol = f_buscar_carol_danvers(cola)
    print(f"\nf) Carol Danvers en la cola: {'Sí' if encontrado else 'No'}")
    if encontrado:
        print(f"   Su superhéroe es: {superheroe_carol}")

    print("\n" + "=" * 55)
