
# -*- coding: utf-8 -*-
"""
Similitud de coseno entre un perfil de usuario y películas.
Versión sin dependencias externas: SOLO diccionarios y librerías estándar.

Uso básico:
    python similitud_coseno.py

Uso con archivos JSON opcionales:
    python similitud_coseno.py --movies movies.json --ratings ratings.json

Estructura esperada de JSON:
- movies.json:
    {
      "Matrix": {"Accion":5,"Romance":1,"Comedia":0,"Ciencia Ficcion":5},
      "Titanic": {"Accion":1,"Romance":5,"Comedia":0,"Ciencia Ficcion":0}
      ...
    }
- ratings.json:
    {
      "Matrix": 5,
      "Avengers": 4,
      ...
    }
"""
from __future__ import annotations
import math, csv, json, argparse, sys
from typing import Dict, List

# -----------------------------
# Utilidades con diccionarios
# -----------------------------
def dot(u: Dict[str, float], m: Dict[str, float], generos: List[str]) -> float:
    return sum(u[g] * m[g] for g in generos)

def norm(v: Dict[str, float], generos: List[str]) -> float:
    return math.sqrt(sum((v[g] or 0.0) ** 2 for g in generos))
def calcular_perfil_u(movie_vectors: Dict[str, Dict[str, float]], ratings: Dict[str, float], generos: List[str]) -> Dict[str, float]:
    """Calcula el perfil de usuario como promedio ponderado de vectores por rating.
    Devuelve un diccionario con la misma clave que `generos`.
    """
    # Inicializar suma ponderada
    weighted_sum = {g: 0.0 for g in generos}
    sum_ratings = 0.0
    for movie, r in ratings.items():
        if movie not in movie_vectors:
            raise KeyError(f"El rating incluye '{movie}' pero no existe en movie_vectors")
        # sumar r * vector_movie por cada género
        for g in generos:
            weighted_sum[g] += float(movie_vectors[movie].get(g, 0.0)) * float(r)
        sum_ratings += float(r)
    if sum_ratings == 0:
        raise ValueError("La suma de ratings es 0")
    # Normalizar por la suma de ratings
    return {g: weighted_sum[g] / sum_ratings for g in generos}

def similitud_coseno(u: Dict[str, float], m: Dict[str, float], generos: List[str]) -> float:
    u_norm = norm(u, generos)
    m_norm = norm(m, generos)
    denom = u_norm * m_norm
    return (dot(u, m, generos) / denom) if denom != 0 else float("nan")

def tabla_resultados(movie_vectors: Dict[str, Dict[str, float]], ratings: Dict[str, float], generos: List[str]):
    u = calcular_perfil_u(movie_vectors, ratings, generos)
    u_norm = norm(u, generos)
    filas = []
    for movie, m in movie_vectors.items():
        dot_um = dot(u, m, generos)
        m_norm = norm(m, generos)
        denom = u_norm * m_norm
        cos_sim = (dot_um / denom) if denom != 0 else float("nan")
        filas.append({
            "Pelicula": movie,
            "Producto punto (u·m)": dot_um,
            "|u|": u_norm,
            "|m|": m_norm,
            "Producto normas (|u|·|m|)": denom,
            "Similitud coseno": cos_sim,
        })
    filas.sort(key=lambda r: r["Similitud coseno"], reverse=True)
    return u, u_norm, filas

def guardar_csv(path: str, filas):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        writer.writeheader()
        for r in filas:
            writer.writerow(r)

def guardar_json(path: str, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def redondear_dict(d: Dict[str, float], ndigits: int = 9):
    return {k: round(v, ndigits) for k, v in d.items()}

def main(argv=None):
    parser = argparse.ArgumentParser(description="Similitud del coseno entre perfil de usuario y películas (solo dicts)")
    parser.add_argument("--movies", type=str, default=None, help="Ruta a JSON con vectores de películas")
    parser.add_argument("--ratings", type=str, default=None, help="Ruta a JSON con ratings")
    parser.add_argument("--out-prefix", type=str, default="salida", help="Prefijo de archivos de salida (CSV/JSON)")
    parser.add_argument("--print", action="store_true", help="Imprime tabla en consola")
    args = parser.parse_args(argv)

    # Géneros por defecto y datos de ejemplo
    generos = ["Accion", "Romance", "Comedia", "Ciencia Ficcion"]
    movie_vectors = {
        "Matrix":     {"Accion": 5, "Romance": 1, "Comedia": 0, "Ciencia Ficcion": 5},
        "Titanic":    {"Accion": 1, "Romance": 5, "Comedia": 0, "Ciencia Ficcion": 0},
        "Avengers":   {"Accion": 5, "Romance": 1, "Comedia": 2, "Ciencia Ficcion": 4},
        "La La Land": {"Accion": 0, "Romance": 5, "Comedia": 2, "Ciencia Ficcion": 0},
        "Deadpool":   {"Accion": 4, "Romance": 1, "Comedia": 5, "Ciencia Ficcion": 1},
    }
    ratings = {"Matrix": 5, "Avengers": 4, "Titanic": 1, "La La Land": 2, "Deadpool": 5}

    # Sobrescribir si se pasan JSONs
    if args.movies:
        with open(args.movies, "r", encoding="utf-8") as f:
            movie_vectors = json.load(f)
    if args.ratings:
        with open(args.ratings, "r", encoding="utf-8") as f:
            ratings = json.load(f)

    # Validación mínima de géneros
    gen0 = next(iter(movie_vectors.values()))
    generos = list(gen0.keys())  # usa los keys del primer vector como orden
    for mname, vec in movie_vectors.items():
        if set(vec.keys()) != set(generos):
            raise ValueError(f"El vector de '{mname}' no coincide en géneros con {generos}")

    u, u_norm, filas = tabla_resultados(movie_vectors, ratings, generos)

    # Guardar salidas
    csv_path = f"{args.out_prefix}_similitud_coseno.csv"
    json_path = f"{args.out_prefix}_resultados.json"
    guardar_csv(csv_path, filas)
    guardar_json(json_path, {
        "generos": generos,
        "perfil_u": u,
        "norma_u": u_norm,
        "resultados": filas
    })

    # Imprimir si se solicita
    if args.print:
        print("Géneros:", generos)
        print("Perfil u:", redondear_dict(u))
        print("Norma de u:", round(u_norm, 9))
        print("\nTabla (ordenada):")
        for r in filas:
            print(f"{r['Pelicula']:>10s} | dot={r['Producto punto (u·m)']:.9f} "
                  f"| |u|={r['|u|']:.9f} | |m|={r['|m|']:.9f} "
                  f"| denom={r['Producto normas (|u|·|m|)']:.9f} "
                  f"| cos={r['Similitud coseno']:.9f}")
        print(f"\nArchivos generados:\n - {csv_path}\n - {json_path}")

if __name__ == "__main__":
    main()
