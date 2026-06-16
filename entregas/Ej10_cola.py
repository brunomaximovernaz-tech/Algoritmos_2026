# Ejercicio 10 - Guía de Cola
# Cola con notificaciones de redes sociales de un Smartphone.
# Cada notificación tiene: hora, aplicación y mensaje.
# Resolver:
#   a) Eliminar todas las notificaciones de Facebook
#   b) Mostrar las notificaciones de Twitter cuyo mensaje incluya 'Python', sin perder datos
#   c) Usar una pila para almacenar las notificaciones entre las 11:43 y las 15:57,
#      y determinar cuántas son


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


# ── TDA Pila ─────────────────────────────────────────────────────────────────

class Pila:
    def __init__(self):
        self.__datos = []

    def apilar(self, elemento):
        self.__datos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.__datos.pop()

    def esta_vacia(self):
        return len(self.__datos) == 0

    def tamanio(self):
        return len(self.__datos)


# ── Funciones auxiliares ──────────────────────────────────────────────────────

def hora_a_minutos(hora_str):
    """Convierte 'HH:MM' a minutos totales para comparar horas fácilmente."""
    h, m = map(int, hora_str.split(":"))
    return h * 60 + m


# ── a) Eliminar notificaciones de Facebook ────────────────────────────────────

def eliminar_facebook(cola):
    """
    Elimina todas las notificaciones de Facebook de la cola.
    Recorre la cola atendiendo cada elemento: si no es de Facebook lo vuelve
    a encolar en una cola auxiliar, luego restaura la cola original.
    """
    aux = Cola()
    eliminadas = 0

    while not cola.cola_vacia():
        notif = cola.atencion()
        if notif["app"].lower() == "facebook":
            eliminadas += 1
        else:
            aux.arribo(notif)

    # Restaurar cola original sin Facebook
    while not aux.cola_vacia():
        cola.arribo(aux.atencion())

    return eliminadas


# ── b) Mostrar notificaciones de Twitter con 'Python' ─────────────────────────

def mostrar_twitter_python(cola):
    """
    Muestra las notificaciones de Twitter cuyo mensaje incluya 'Python',
    sin perder los datos de la cola.
    """
    aux = Cola()
    encontradas = []

    while not cola.cola_vacia():
        notif = cola.atencion()
        if notif["app"].lower() == "twitter" and "python" in notif["mensaje"].lower():
            encontradas.append(notif)
        aux.arribo(notif)

    # Restaurar cola original
    while not aux.cola_vacia():
        cola.arribo(aux.atencion())

    return encontradas


# ── c) Notificaciones entre 11:43 y 15:57 almacenadas en pila ────────────────

def notificaciones_en_pila(cola):
    """
    Recorre la cola y apila las notificaciones producidas entre las 11:43 y las 15:57.
    Restaura la cola original y retorna la pila con las notificaciones del rango
    junto con la cantidad.
    """
    aux = Cola()
    pila = Pila()
    inicio = hora_a_minutos("11:43")
    fin = hora_a_minutos("15:57")

    while not cola.cola_vacia():
        notif = cola.atencion()
        hora = hora_a_minutos(notif["hora"])
        if inicio <= hora <= fin:
            pila.apilar(notif)
        aux.arribo(notif)

    # Restaurar cola original
    while not aux.cola_vacia():
        cola.arribo(aux.atencion())

    return pila


# ── Programa principal ────────────────────────────────────────────────────────

if __name__ == "__main__":

    # Datos de prueba
    notificaciones = [
        {"hora": "08:15", "app": "Twitter",   "mensaje": "Nuevo seguidor"},
        {"hora": "09:30", "app": "Facebook",  "mensaje": "Te etiquetaron en una foto"},
        {"hora": "10:00", "app": "Instagram", "mensaje": "Nueva historia"},
        {"hora": "11:43", "app": "Twitter",   "mensaje": "Tendencia: Python en IA"},
        {"hora": "12:05", "app": "Facebook",  "mensaje": "Comentario en tu publicación"},
        {"hora": "13:20", "app": "Twitter",   "mensaje": "Python 4.0 anunciado"},
        {"hora": "14:00", "app": "WhatsApp",  "mensaje": "Hola, cómo estás?"},
        {"hora": "15:57", "app": "Twitter",   "mensaje": "Curso de Python gratis"},
        {"hora": "16:30", "app": "Facebook",  "mensaje": "Cumpleaños de un amigo"},
        {"hora": "17:45", "app": "Instagram", "mensaje": "Nueva publicación"},
    ]

    cola = Cola()
    for n in notificaciones:
        cola.arribo(n)

    print("=" * 55)
    print("   COLA DE NOTIFICACIONES - SMARTPHONE")
    print("=" * 55)
    print(f"Total de notificaciones cargadas: {cola.tamanio()}\n")

    # a) Eliminar Facebook
    eliminadas = eliminar_facebook(cola)
    print(f"a) Notificaciones de Facebook eliminadas: {eliminadas}")
    print(f"   Notificaciones restantes en la cola: {cola.tamanio()}\n")

    # b) Twitter con 'Python'
    twitter_python = mostrar_twitter_python(cola)
    print(f"b) Notificaciones de Twitter con 'Python': {len(twitter_python)}")
    for n in twitter_python:
        print(f"   [{n['hora']}] {n['app']}: {n['mensaje']}")

    # c) Pila con notificaciones entre 11:43 y 15:57
    pila = notificaciones_en_pila(cola)
    print(f"\nc) Notificaciones entre 11:43 y 15:57 almacenadas en pila: {pila.tamanio()}")
    print("   Contenido de la pila (tope → fondo):")
    aux_pila = Pila()
    while not pila.esta_vacia():
        n = pila.desapilar()
        print(f"   [{n['hora']}] {n['app']}: {n['mensaje']}")
        aux_pila.apilar(n)

    print("\n" + "=" * 55)
