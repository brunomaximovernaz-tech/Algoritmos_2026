from tree import BinaryTree
from pokemon_data import pokemons

# 1. Crear los 3 árboles
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# Insertar en los árboles iterando la lista importada
for p in pokemons:
    arbol_nombre.insert_node(p.nombre, p)
    arbol_numero.insert_node(p.numero, p)
    for tipo in p.tipos:
        arbol_tipo.insert_node(tipo, p)

print("="*50)
print("1. MOSTRAR DATOS POR NÚMERO Y PROXIMIDAD DE NOMBRE")
# Búsqueda exacta por número
num_buscado = 97
nodo = arbol_numero.search(num_buscado)
if nodo: print(f"Por número {num_buscado}: {nodo.other_values}")

# Búsqueda por proximidad de nombre ("bul")
print("\nBúsqueda por proximidad ('bul'):")
def proxy_search_full(root, prefix):
    if root is not None:
        proxy_search_full(root.left, prefix)
        if prefix.lower() in str(root.value).lower():
            print(root.other_values)
        proxy_search_full(root.right, prefix)
proxy_search_full(arbol_nombre.root, "bul")

print("\n"+"="*50)
print("2. POKÉMONS DE TIPO FANTASMA, FUEGO, ACERO Y ELÉCTRICO")
def inorden_tipo(root, tipos_buscados):
    if root is not None:
        inorden_tipo(root.left, tipos_buscados)
        if root.value in tipos_buscados:
            print(f"[{root.value}] {root.other_values.nombre}")
        inorden_tipo(root.right, tipos_buscados)
inorden_tipo(arbol_tipo.root, ["Fantasma", "Fuego", "Acero", "Eléctrico"])

print("\n"+"="*50)
print("3. LISTADOS ASCENDENTES Y POR NIVEL")
print("Listado ascendente por NÚMERO (Primeros 10 para no saturar):")
def inorden_limit(root, limit, count=[0]):
    if root is not None and count[0] < limit:
        inorden_limit(root.left, limit, count)
        if count[0] < limit:
            print(root.other_values.nombre)
            count[0] += 1
        inorden_limit(root.right, limit, count)
inorden_limit(arbol_numero.root, 10)

print("\nListado ascendente por NOMBRE (Primeros 10):")
inorden_limit(arbol_nombre.root, 10, [0])

print("\nListado por NIVEL por NOMBRE:")
arbol_nombre.by_level() 

print("\n"+"="*50)
print("4. DÉBILES FRENTE A JOLTEON (Eléctrico), LYCANROC (Roca), TYRANTRUM (Roca/Dragón)")
tipos_atacantes = ["Eléctrico", "Roca", "Dragón"]
def inorden_debilidades(root):
    if root is not None:
        inorden_debilidades(root.left)
        if any(debilidad in tipos_atacantes for debilidad in root.other_values.debilidades):
            print(f"{root.other_values.nombre} es débil contra al menos uno de ellos.")
        inorden_debilidades(root.right)
inorden_debilidades(arbol_nombre.root)

print("\n"+"="*50)
print("5. TIPOS DE POKÉMON Y CUÁNTOS HAY DE CADA UNO")
dic_tipos = {}
def contar_tipos(root):
    if root is not None:
        contar_tipos(root.left)
        dic_tipos[root.value] = dic_tipos.get(root.value, 0) + 1
        contar_tipos(root.right)
contar_tipos(arbol_tipo.root)
for tipo, cant in dic_tipos.items():
    print(f"Tipo {tipo}: {cant} Pokémons")

print("\n"+"="*50)
print("6. CANTIDAD DE MEGAEVOLUCIONES Y FORMAS GIGAMAX")
def contar_megas_gigas(root, contadores):
    if root is not None:
        contar_megas_gigas(root.left, contadores)
        if root.other_values.mega: contadores['mega'] += 1
        if root.other_values.gigamax: contadores['giga'] += 1
        contar_megas_gigas(root.right, contadores)

totales = {'mega': 0, 'giga': 0}
contar_megas_gigas(arbol_nombre.root, totales)
print(f"Pokémons con Megaevolución: {totales['mega']}")
print(f"Pokémons con Gigamax: {totales['giga']}")