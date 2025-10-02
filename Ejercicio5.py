"""
EJERCICIO 5: IMPUTACIÓN POR MEDIANA AGRUPADA POR CURSO
======================================================

Estudio de calificaciones de proyecto final por curso usando imputación por mediana
para reducir la influencia de valores atípicos y preservar la tendencia central de cada curso.

"""

import numpy as np
import pandas as pd

# Datos de calificaciones de proyecto final por curso
calificaciones_ds = {
    "calificaciones_curso_a": [3.0, 3.5, 4.0, np.nan, 3.8, 3.2, 3.5, 3.0, np.nan, 3.6, 
                               3.7, np.nan, 3.4, 3.5, 3.8, 3.0, 3.6, np.nan, 3.2, 3.5],
    "calificaciones_curso_b": [4.5, 4.7, 4.8, np.nan, 4.9, 4.6, 4.8, 4.7, np.nan, 4.9, 
                               4.5, 4.8, np.nan, 4.7, 4.9, 4.6, 4.8, 4.7, np.nan, 4.9],
    "calificaciones_curso_c": [2.8, 3.0, 3.2, np.nan, 2.9, 3.1, 3.0, 2.8, np.nan, 3.2, 
                               3.1, np.nan, 2.9, 3.0, 3.1, 2.8, 3.2, np.nan, 2.9, 3.0]
}

def main():
    """
    Función principal que ejecuta el análisis de calificaciones por curso.
    """
    
    print("EJERCICIO 5: IMPUTACIÓN POR MEDIANA AGRUPADA POR CURSO")
    print("=" * 56)
    
    # 1. Crear DataFrame
    calificaciones_df = pd.DataFrame(calificaciones_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(calificaciones_df)
    print("_" * 40)
    print(f"Dimensiones: {calificaciones_df.shape}")
    
    # 2. Calcular medianas por curso
    print("\n=== MEDIANAS DE CALIFICACIONES POR CURSO ===")
    medianas = {}
    for curso in calificaciones_df.columns:
        mediana = calificaciones_df[curso].median()
        medianas[curso] = mediana
        nombre = curso.replace('calificaciones_', '').replace('_', ' ').title()
        print(f"{nombre}: {mediana:.2f} puntos")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medianas
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    calificaciones_imputadas = calificaciones_df.copy()
    
    # Imputar cada columna con su respectiva mediana
    for curso in calificaciones_df.columns:
        calificaciones_imputadas[curso] = calificaciones_df[curso].fillna(medianas[curso])
        n_imputados = calificaciones_df[curso].isna().sum()
        nombre = curso.replace('calificaciones_', '').replace('_', ' ').title()
        print(f"✓ {nombre}: {n_imputados} valores imputados con {medianas[curso]:.2f} puntos")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = calificaciones_imputadas.round(2)
    datos_mostrar.columns = [col.replace('calificaciones_', '').replace('_', ' ').title() for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {calificaciones_imputadas.isna().sum().sum()}")
    print("=" * 56)
    
    return calificaciones_imputadas

if __name__ == "__main__":
    datos_final = main()