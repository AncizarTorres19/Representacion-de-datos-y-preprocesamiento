# ejercicio1_conLibrerias.py
# Ejercicio 1 - Similitud coseno con NumPy
# Instrucciones:
#   - Ejecuta este archivo con:  python ejercicio1_conLibrerias.py
#   - Requiere tener NumPy instalado: pip install numpy
#   - El script imprimirá el ranking de canciones según su similitud coseno

import numpy as np

# Vector del usuario (Pop, Rock, Jazz, Electrónica, Clásica)
usuario = np.array([4, 5, 1, 3, 0], dtype=float)

# Canciones y sus vectores en el orden [Pop, Rock, Jazz, Electrónica, Clásica]
canciones = {
    "Blinding Lights":            np.array([5, 2, 0, 5, 0], dtype=float),
    "Bohemian Rhapsody":          np.array([3, 5, 1, 0, 1], dtype=float),
    "Take Five":                  np.array([0, 1, 5, 0, 3], dtype=float),
    "Shape of You":               np.array([5, 1, 0, 4, 0], dtype=float),
    "Smells Like Teen Spirit":    np.array([1, 5, 0, 1, 0], dtype=float),
    "Blue in Green":              np.array([0, 0, 5, 0, 5], dtype=float),
    "Strobe":                     np.array([2, 1, 0, 5, 0], dtype=float),
    "Fur Elise":                  np.array([0, 0, 1, 0, 5], dtype=float),
    "Radioactive":                np.array([4, 5, 0, 3, 0], dtype=float),
    "Rolling in the Deep":        np.array([5, 3, 0, 1, 0], dtype=float),
    "Moonlight Sonata":           np.array([0, 0, 0, 0, 5], dtype=float),
    "Clocks":                     np.array([3, 4, 0, 4, 0], dtype=float),
    "Uptown Funk":                np.array([5, 2, 1, 4, 0], dtype=float),
    "Imagine":                    np.array([4, 3, 0, 0, 1], dtype=float),
    "Fly Me to the Moon":         np.array([2, 1, 5, 0, 2], dtype=float),
}

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))

def rank_by_similarity(user_vec: np.ndarray, items: dict) -> list:
    resultados = [(name, cosine_similarity(user_vec, vec)) for name, vec in items.items()]
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

if __name__ == "__main__":
    ranking = rank_by_similarity(usuario, canciones)
    print("Ranking por similitud coseno (mayor a menor):\n")
    for nombre, sim in ranking:
        print(f"{nombre:25s}  ->  {sim:.6f}")
