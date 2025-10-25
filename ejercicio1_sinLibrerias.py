# ejercicio1_sinLibrerias.py
# Ejercicio 1 - Similitud coseno (sin librerías)
# Instrucciones:
#   - Ejecuta este archivo con:  python ejercicio1_sinLibrerias.py
#   - El script imprimirá el ranking de canciones según su similitud coseno
# Datos tomados del enunciado (canciones vs. géneros): Pop, Rock, Jazz, Electrónica, Clásica

from math import sqrt

# Vector del usuario (Pop, Rock, Jazz, Electrónica, Clásica)
usuario = [4, 5, 1, 3, 0]

# Canciones y sus vectores en el orden [Pop, Rock, Jazz, Electrónica, Clásica]
canciones = {
    "Blinding Lights":            [5, 2, 0, 5, 0],
    "Bohemian Rhapsody":          [3, 5, 1, 0, 1],
    "Take Five":                  [0, 1, 5, 0, 3],
    "Shape of You":               [5, 1, 0, 4, 0],
    "Smells Like Teen Spirit":    [1, 5, 0, 1, 0],
    "Blue in Green":              [0, 0, 5, 0, 5],
    "Strobe":                     [2, 1, 0, 5, 0],
    "Fur Elise":                  [0, 0, 1, 0, 5],
    "Radioactive":                [4, 5, 0, 3, 0],
    "Rolling in the Deep":        [5, 3, 0, 1, 0],
    "Moonlight Sonata":           [0, 0, 0, 0, 5],
    "Clocks":                     [3, 4, 0, 4, 0],
    "Uptown Funk":                [5, 2, 1, 4, 0],
    "Imagine":                    [4, 3, 0, 0, 1],
    "Fly Me to the Moon":         [2, 1, 5, 0, 2],
}

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def norm(a):
    return sqrt(sum(x*x for x in a))

def cosine_similarity(a, b):
    na = norm(a)
    nb = norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return dot(a, b) / (na * nb)

def rank_by_similarity(user_vec, items):
    resultados = []
    for nombre, vec in items.items():
        sim = cosine_similarity(user_vec, vec)
        resultados.append((nombre, sim))
    # Ordenar de mayor a menor similitud
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

if __name__ == "__main__":
    ranking = rank_by_similarity(usuario, canciones)
    print("Ranking por similitud coseno (mayor a menor):\n")
    for nombre, sim in ranking:
        print(f"{nombre:25s}  ->  {sim:.6f}")
