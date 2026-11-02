from graph import Graph
from star_wars_data import personajes_sw, relaciones_sw

# Instanciamos el Grafo NO dirigido
g = Graph(is_dir=False)

# 1. Cargar los vértices (personajes)
for p in personajes_sw:
    # Usamos other_values para guardar el diccionario completo y tener a mano los episodios
    g.add_vertex(p["nombre"], other_values=p)

# 2. Cargar las aristas (relaciones y pesos)
for peso, origen, destino in relaciones_sw:
    g.add_edge(peso, origen, destino)

print("="*60)
print("1. ÁRBOL DE EXPANSIÓN MÍNIMO DESDE C-3PO, YODA Y LEIA")
print("="*60)
# Usamos el método kruskal del profe pasándole el vértice origen
for origen in ["C-3PO", "Yoda", "Leia"]:
    print(f"\nKruskal (Árbol de expansión mínimo) desde {origen}:")
    arbol_min = g.kruskal(origen)
    print(arbol_min)

print("\n" + "="*60)
print("2. NÚMERO MÁXIMO DE EPISODIOS COMPARTIDOS Y PARES")
print("="*60)
max_eps = -1
pares = []

# Iteramos usando la estructura del TDA del profe
for v in g:
    for arista in v.edges:
        if arista.weight > max_eps:
            max_eps = arista.weight
            pares = [(v.value, arista.destination)]
        elif arista.weight == max_eps:
            # Evitar duplicados porque es no dirigido (ej: A-B y B-A)
            if (arista.destination, v.value) not in pares:
                pares.append((v.value, arista.destination))

print(f"El máximo de episodios compartidos es: {max_eps}")
print("Personajes que comparten esa cantidad:")
for p1, p2 in pares:
    print(f" - {p1} y {p2}")

print("\n" + "="*60)
print("3. CAMINO MÁS CORTO (Dijkstra)")
print("="*60)
# Adaptación exacta del método de extracción de camino que hace el profe en prueba_tree.py
def calcular_camino(origen, destino):
    if g.exist_path(origen, destino):
        pila_camino = g.dijkstra(origen)
        camino = []
        peso_total = None
        dest_actual = destino
        
        while pila_camino.size() > 0:
            paso = pila_camino.pop()
            if paso[0] == dest_actual:
                if peso_total is None:
                    peso_total = paso[1]
                camino.append(paso[0])
                dest_actual = paso[2]
                
        camino.reverse()
        print(f"De {origen} a {destino}")
        print(f" -> Camino: {' - '.join(camino)}")
        print(f" -> Distancia (episodios compartidos): {peso_total}\n")
    else:
        print(f"No hay camino conectado entre {origen} y {destino}\n")

calcular_camino("C-3PO", "R2-D2")
calcular_camino("Yoda", "Darth Vader")

print("="*60)
print("4. PERSONAJES QUE APARECIERON EN LOS 9 EPISODIOS")
print("="*60)
for v in g:
    # Accedemos a la data original almacenada en other_values
    if v.other_values["episodios"] == 9:
        print(f" - {v.value}")