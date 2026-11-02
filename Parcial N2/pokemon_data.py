class Pokemon:
    def __init__(self, nombre, numero, tipos, debilidades, mega, gigamax):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos
        self.debilidades = debilidades
        self.mega = mega
        self.gigamax = gigamax

    def __str__(self):
        return f"#{self.numero} {self.nombre} | Tipos: {self.tipos} | Débil a: {self.debilidades} | Mega: {self.mega} | Giga: {self.gigamax}"

# Base de datos de 102 Pokémons reales (incluyendo los solicitados en el parcial)
pokemons = [
    # Generación 1
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    Pokemon("Ivysaur", 2, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], False, False),
    Pokemon("Venusaur", 3, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"], True, True),
    Pokemon("Charmander", 4, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Charmeleon", 5, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Charizard", 6, ["Fuego", "Volador"], ["Agua", "Eléctrico", "Roca"], True, True),
    Pokemon("Squirtle", 7, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Wartortle", 8, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Blastoise", 9, ["Agua"], ["Planta", "Eléctrico"], True, True),
    Pokemon("Caterpie", 10, ["Bicho"], ["Fuego", "Volador", "Roca"], False, False),
    Pokemon("Metapod", 11, ["Bicho"], ["Fuego", "Volador", "Roca"], False, False),
    Pokemon("Butterfree", 12, ["Bicho", "Volador"], ["Fuego", "Volador", "Roca", "Eléctrico", "Hielo"], False, True),
    Pokemon("Weedle", 13, ["Bicho", "Veneno"], ["Fuego", "Volador", "Roca", "Psíquico"], False, False),
    Pokemon("Kakuna", 14, ["Bicho", "Veneno"], ["Fuego", "Volador", "Roca", "Psíquico"], False, False),
    Pokemon("Beedrill", 15, ["Bicho", "Veneno"], ["Fuego", "Volador", "Roca", "Psíquico"], True, False),
    Pokemon("Pidgey", 16, ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    Pokemon("Pidgeotto", 17, ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], False, False),
    Pokemon("Pidgeot", 18, ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"], True, False),
    Pokemon("Rattata", 19, ["Normal"], ["Lucha"], False, False),
    Pokemon("Raticate", 20, ["Normal"], ["Lucha"], False, False),
    Pokemon("Pikachu", 25, ["Eléctrico"], ["Tierra"], False, True),
    Pokemon("Raichu", 26, ["Eléctrico"], ["Tierra"], False, False),
    Pokemon("Sandshrew", 27, ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    Pokemon("Sandslash", 28, ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    Pokemon("Vulpix", 37, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Ninetales", 38, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Jigglypuff", 39, ["Normal", "Hada"], ["Veneno", "Acero"], False, False),
    Pokemon("Wigglytuff", 40, ["Normal", "Hada"], ["Veneno", "Acero"], False, False),
    Pokemon("Zubat", 41, ["Veneno", "Volador"], ["Eléctrico", "Hielo", "Psíquico", "Roca"], False, False),
    Pokemon("Golbat", 42, ["Veneno", "Volador"], ["Eléctrico", "Hielo", "Psíquico", "Roca"], False, False),
    Pokemon("Meowth", 52, ["Normal"], ["Lucha"], False, True),
    Pokemon("Persian", 53, ["Normal"], ["Lucha"], False, False),
    Pokemon("Psyduck", 54, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Golduck", 55, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Mankey", 56, ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    Pokemon("Primeape", 57, ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    Pokemon("Growlithe", 58, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Arcanine", 59, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Abra", 63, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    Pokemon("Kadabra", 64, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    Pokemon("Alakazam", 65, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], True, False),
    Pokemon("Machop", 66, ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    Pokemon("Machoke", 67, ["Lucha"], ["Volador", "Psíquico", "Hada"], False, False),
    Pokemon("Machamp", 68, ["Lucha"], ["Volador", "Psíquico", "Hada"], False, True),
    Pokemon("Geodude", 74, ["Roca", "Tierra"], ["Agua", "Planta", "Hielo", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Graveler", 75, ["Roca", "Tierra"], ["Agua", "Planta", "Hielo", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Golem", 76, ["Roca", "Tierra"], ["Agua", "Planta", "Hielo", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Magnemite", 81, ["Eléctrico", "Acero"], ["Tierra", "Fuego", "Lucha"], False, False),
    Pokemon("Magneton", 82, ["Eléctrico", "Acero"], ["Tierra", "Fuego", "Lucha"], False, False),
    Pokemon("Gastly", 92, ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"], False, False),
    Pokemon("Haunter", 93, ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"], False, False),
    Pokemon("Gengar", 94, ["Fantasma", "Veneno"], ["Fantasma", "Siniestro", "Psíquico", "Tierra"], True, True),
    Pokemon("Onix", 95, ["Roca", "Tierra"], ["Agua", "Planta", "Hielo", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Cubone", 104, ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    Pokemon("Marowak", 105, ["Tierra"], ["Agua", "Planta", "Hielo"], False, False),
    Pokemon("Rhyhorn", 111, ["Tierra", "Roca"], ["Agua", "Planta", "Hielo", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Rhydon", 112, ["Tierra", "Roca"], ["Agua", "Planta", "Hielo", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Scyther", 123, ["Bicho", "Volador"], ["Fuego", "Volador", "Roca", "Eléctrico", "Hielo"], False, False),
    Pokemon("Pinsir", 127, ["Bicho"], ["Fuego", "Volador", "Roca"], True, False),
    Pokemon("Magikarp", 129, ["Agua"], ["Planta", "Eléctrico"], False, False),
    Pokemon("Gyarados", 130, ["Agua", "Volador"], ["Eléctrico", "Roca"], True, False),
    Pokemon("Lapras", 131, ["Agua", "Hielo"], ["Planta", "Eléctrico", "Lucha", "Roca"], False, True),
    Pokemon("Eevee", 133, ["Normal"], ["Lucha"], False, True),
    Pokemon("Vaporeon", 134, ["Agua"], ["Planta", "Eléctrico"], False, False),
    # REQUISITO DEL PARCIAL:
    Pokemon("Jolteon", 135, ["Eléctrico"], ["Tierra"], False, False),
    Pokemon("Flareon", 136, ["Fuego"], ["Agua", "Tierra", "Roca"], False, False),
    Pokemon("Snorlax", 143, ["Normal"], ["Lucha"], False, True),
    Pokemon("Articuno", 144, ["Hielo", "Volador"], ["Fuego", "Eléctrico", "Roca", "Acero"], False, False),
    Pokemon("Zapdos", 145, ["Eléctrico", "Volador"], ["Hielo", "Roca"], False, False),
    Pokemon("Moltres", 146, ["Fuego", "Volador"], ["Agua", "Eléctrico", "Roca"], False, False),
    Pokemon("Dratini", 147, ["Dragón"], ["Hielo", "Dragón", "Hada"], False, False),
    Pokemon("Dragonair", 148, ["Dragón"], ["Hielo", "Dragón", "Hada"], False, False),
    Pokemon("Dragonite", 149, ["Dragón", "Volador"], ["Hielo", "Dragón", "Hada", "Roca"], False, False),
    Pokemon("Mewtwo", 150, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], True, False),
    Pokemon("Mew", 151, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"], False, False),
    
    # Generaciones posteriores (Selección mixta para cubrir Acero, Fantasma, etc.)
    Pokemon("Steelix", 208, ["Acero", "Tierra"], ["Fuego", "Agua", "Lucha", "Tierra"], True, False),
    Pokemon("Scizor", 212, ["Bicho", "Acero"], ["Fuego"], True, False),
    Pokemon("Skarmory", 227, ["Acero", "Volador"], ["Fuego", "Eléctrico"], False, False),
    Pokemon("Houndour", 228, ["Siniestro", "Fuego"], ["Agua", "Lucha", "Tierra", "Roca"], False, False),
    Pokemon("Houndoom", 229, ["Siniestro", "Fuego"], ["Agua", "Lucha", "Tierra", "Roca"], True, False),
    Pokemon("Tyranitar", 248, ["Roca", "Siniestro"], ["Lucha", "Bicho", "Planta", "Agua", "Hada", "Tierra", "Acero"], True, False),
    Pokemon("Lugia", 249, ["Psíquico", "Volador"], ["Eléctrico", "Hielo", "Roca", "Fantasma", "Siniestro"], False, False),
    Pokemon("Ho-Oh", 250, ["Fuego", "Volador"], ["Agua", "Eléctrico", "Roca"], False, False),
    Pokemon("Mawile", 303, ["Acero", "Hada"], ["Fuego", "Tierra"], True, False),
    Pokemon("Aron", 304, ["Acero", "Roca"], ["Fuego", "Agua", "Lucha", "Tierra"], False, False),
    Pokemon("Lairon", 305, ["Acero", "Roca"], ["Fuego", "Agua", "Lucha", "Tierra"], False, False),
    Pokemon("Aggron", 306, ["Acero", "Roca"], ["Fuego", "Agua", "Lucha", "Tierra"], True, False),
    Pokemon("Banette", 354, ["Fantasma"], ["Fantasma", "Siniestro"], True, False),
    Pokemon("Duskull", 355, ["Fantasma"], ["Fantasma", "Siniestro"], False, False),
    Pokemon("Dusclops", 356, ["Fantasma"], ["Fantasma", "Siniestro"], False, False),
    Pokemon("Metagross", 376, ["Acero", "Psíquico"], ["Fuego", "Tierra", "Fantasma", "Siniestro"], True, False),
    Pokemon("Lucario", 448, ["Lucha", "Acero"], ["Fuego", "Lucha", "Tierra"], True, False),
    Pokemon("Rotom", 479, ["Eléctrico", "Fantasma"], ["Siniestro", "Fantasma"], False, False),
    Pokemon("Dialga", 483, ["Acero", "Dragón"], ["Lucha", "Tierra"], False, False),
    Pokemon("Chandelure", 609, ["Fantasma", "Fuego"], ["Agua", "Tierra", "Roca", "Fantasma", "Siniestro"], False, False),
    Pokemon("Aegislash", 681, ["Acero", "Fantasma"], ["Fuego", "Tierra", "Fantasma", "Siniestro"], False, False),
    
    # REQUISITO DEL PARCIAL:
    Pokemon("Tyrunt", 696, ["Roca", "Dragón"], ["Hielo", "Lucha", "Tierra", "Dragón", "Acero", "Hada"], False, False),
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"], ["Hielo", "Lucha", "Tierra", "Dragón", "Acero", "Hada"], False, False),
    
    Pokemon("Mimikyu", 778, ["Fantasma", "Hada"], ["Fantasma", "Acero"], False, False),
    
    # REQUISITO DEL PARCIAL:
    Pokemon("Rockruff", 744, ["Roca"], ["Agua", "Planta", "Lucha", "Tierra", "Acero"], False, False),
    Pokemon("Lycanroc", 745, ["Roca"], ["Agua", "Planta", "Lucha", "Tierra", "Acero"], False, False),
    
    Pokemon("Corviknight", 823, ["Volador", "Acero"], ["Fuego", "Eléctrico"], False, True),
    Pokemon("Toxtricity", 849, ["Eléctrico", "Veneno"], ["Tierra", "Psíquico"], False, True)
]