
# -*- coding: utf-8 -*-
"""
Similitud de coseno entre un perfil de usuario y películas.
"""
import math

def dot(u, m, generos):
    return sum(u[g] * m[g] for g in generos)

def norm(v, generos):
    return math.sqrt(sum((v[g] or 0.0) ** 2 for g in generos))

def calcular_perfil_u(movie_vectors, ratings, generos):
    """Calcula el perfil de usuario como promedio ponderado de vectores por rating."""
    weighted_sum = {g: 0.0 for g in generos}
    sum_ratings = 0.0
    for movie, r in ratings.items():
        if movie not in movie_vectors:
            raise KeyError(f"El rating incluye '{movie}' pero no existe en movie_vectors")
        for g in generos:
            weighted_sum[g] += float(movie_vectors[movie].get(g, 0.0)) * float(r)
        sum_ratings += float(r)
    if sum_ratings == 0:
        raise ValueError("La suma de ratings es 0")
    return {g: weighted_sum[g] / sum_ratings for g in generos}

def similitud_coseno(u, m, generos):
    u_norm = norm(u, generos)
    m_norm = norm(m, generos)
    denom = u_norm * m_norm
    return (dot(u, m, generos) / denom) if denom != 0 else float("nan")

def tabla_resultados(movie_vectors, ratings, generos):
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

def redondear_dict(d, ndigits=9):
    return {k: round(v, ndigits) for k, v in d.items()}

# -----------------------------
# Función principal
# -----------------------------
if __name__ == "__main__":
    # Vectores de géneros de películas
    movie_vectors = {
        "Matrix":     {"Accion": 5, "Romance": 1, "Comedia": 0, "Ciencia Ficcion": 5},
        "Titanic":    {"Accion": 1, "Romance": 5, "Comedia": 0, "Ciencia Ficcion": 0},
        "Avengers":   {"Accion": 5, "Romance": 1, "Comedia": 2, "Ciencia Ficcion": 4},
        "La La Land": {"Accion": 0, "Romance": 5, "Comedia": 2, "Ciencia Ficcion": 0},
        "Deadpool":   {"Accion": 4, "Romance": 1, "Comedia": 5, "Ciencia Ficcion": 1},
    }
    
    # Ratings del usuario
    ratings = {"Matrix": 5, "Avengers": 4, "Titanic": 1, "La La Land": 2, "Deadpool": 5}
    
    # Géneros
    generos = ["Accion", "Romance", "Comedia", "Ciencia Ficcion"]
    
    u, u_norm, filas = tabla_resultados(movie_vectors, ratings, generos)
    
    # Mostrar resultados en consola
    print("Géneros:", generos)
    print("Perfil u:", redondear_dict(u))
    print("Norma de u:", round(u_norm, 9))
    print("\nTabla (ordenada por similitud coseno):")
    for r in filas:
        print(f"{r['Pelicula']:>10s} | dot={r['Producto punto (u·m)']:.9f} "
              f"| |u|={r['|u|']:.9f} | |m|={r['|m|']:.9f} "
              f"| denom={r['Producto normas (|u|·|m|)']:.9f} "
              f"| cos={r['Similitud coseno']:.9f}")
