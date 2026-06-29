from super_heroes_data import superheroes

lista_heroes = [h["name"] for h in superheroes[:14]] + ["Captain America"]


def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Captain America":
        return True
    return buscar_capitan_america(lista, indice + 1)


def listar_heroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(f"  {indice + 1}. {lista[indice]}")
    listar_heroes(lista, indice + 1)


print("=" * 50)
print("EJERCICIO 1")
print("=" * 50)
print("\nListado de superhéroes:")
listar_heroes(lista_heroes)

encontrado = buscar_capitan_america(lista_heroes)
print(f"\n¿Capitán América está en la lista? {'Sí' if encontrado else 'No'}")
print("=" * 50)
