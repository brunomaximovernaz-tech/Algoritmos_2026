from super_heroes_data import superheroes
from typing import Any

# TDA Cola (implementación de cátedra) 

class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    def attention(self) -> Any:
        return self.__elements.pop(0)

    def size(self) -> int:
        return len(self.__elements)

    def on_front(self) -> Any:
        return self.__elements[0]

    def move_to_end(self) -> Any:
        value = self.__elements.pop(0)
        self.__elements.append(value)
        return value

    def show(self) -> None:
        for i in range(len(self.__elements)):
            value = self.move_to_end()
            print(value)


print("=" * 60)
print("EJERCICIO 2")
print(f"Total de personajes: {len(superheroes)}")
print("=" * 60)

#  1. Listado ordenado ascendente por nombre


print("\n1. Listado ordenado por nombre (ascendente):")
for h in sorted(superheroes, key=lambda h: h["name"].lower()):
    print(f"   {h['name']}")


# 2. Posición de The Thing y Rocket Raccoon

print("\n2. Posición en la lista:")
for nombre in ["The Thing", "Rocket Raccoon"]:
    for i, h in enumerate(superheroes):
        if h["name"] == nombre:
            print(f"   {nombre}: posición {i + 1}")
            break


# 3. Listado de villanos


print("\n3. Villanos:")
villanos = [h for h in superheroes if h["is_villain"]]
for v in villanos:
    print(f"   {v['name']}")

# 4. Villanos en cola → aparecidos antes de 1980

print("\n4. Villanos en cola — aparecieron antes de 1980:")
cola_villanos = Queue()
for v in villanos:
    cola_villanos.arrive(v)

antes_1980 = []
tamanio = cola_villanos.size()
for _ in range(tamanio):
    v = cola_villanos.attention()
    if v["first_appearance"] < 1980:
        antes_1980.append(v)
    cola_villanos.arrive(v)

for v in antes_1980:
    print(f"   {v['name']} ({v['first_appearance']})")


# 5. Superhéroes que comienzan con Bl, G, My, W

print("\n5. Superhéroes que comienzan con Bl, G, My o W:")
for h in superheroes:
    if h["name"].startswith(("Bl", "G", "My", "W")):
        print(f"   {h['name']}")

#  6. Ordenado por nombre real (ascendente)

print("\n6. Ordenado por nombre real (ascendente):")
for h in sorted(superheroes, key=lambda h: (h["real_name"] or "").lower()):
    print(f"   {h['real_name']} — {h['name']}")

#  7. Ordenado por fecha de aparición

print("\n7. Ordenado por fecha de aparición:")
for h in sorted(superheroes, key=lambda h: h["first_appearance"]):
    print(f"   {h['first_appearance']} — {h['name']}")


#  8. Modificar nombre real de Ant Man

print("\n8. Modificar nombre real de Ant Man:")
for h in superheroes:
    if h["name"] == "Ant Man":
        print(f"   Antes:   {h['real_name']}")
        h["real_name"] = "Scott Lang"
        print(f"   Después: {h['real_name']}")
        break


#  9. Biografías con 'time-traveling' o 'suit'

print("\n9. Personajes con 'time-traveling' o 'suit' en su biografía:")
for h in superheroes:
    palabras = [p for p in ["time-traveling", "suit"] if p in h["short_bio"].lower()]
    if palabras:
        print(f"   {h['name']} — {', '.join(palabras)}")


#  10. Eliminar Electro y Baron Zemo 

print("\n10. Eliminar Electro y Baron Zemo:")
for nombre in ["Electro", "Baron Zemo"]:
    for i, h in enumerate(superheroes):
        if h["name"] == nombre:
            eliminado = superheroes.pop(i)
            print(f"   Eliminado: {eliminado['name']}")
            print(f"     Alias       : {eliminado['alias']}")
            print(f"     Nombre real : {eliminado['real_name']}")
            print(f"     Aparición   : {eliminado['first_appearance']}")
            print(f"     Villano     : {eliminado['is_villain']}")
            print(f"     Biografía   : {eliminado['short_bio']}")
            break
    else:
        print(f"   {nombre} no estaba en la lista.")

print(f"\nTotal tras eliminaciones: {len(superheroes)}")
print("=" * 60)
