"""
EJERCICIO 1: IMPUTACIÓN POR MEDIA AGRUPADA POR CIUDAD
====================================================

Estudio de salarios por ciudad en Colombia usando imputación por media
para preservar las características salariales específicas de cada ciudad.

"""

import numpy as np
import pandas as pd

# Datos de salarios por ciudad (en millones de pesos)
salarios_ds = {
    "salarios_bogota": [2.5, 3.0, np.nan, 2.8, 3.1, 2.9, 3.3, np.nan, 2.7, 3.4, 
                        3.0, np.nan, 2.6, 2.8, 3.2, 3.0, np.nan, 2.9, 3.1, 2.7],
    "salarios_cali": [1.8, 2.0, 2.1, np.nan, 1.9, 2.2, 2.3, 2.0, 1.7, np.nan, 
                      2.1, 2.0, np.nan, 1.8, 2.4, 2.1, 2.2, 1.9, 2.0, np.nan],
    "salarios_medellin": [3.5, 3.7, 3.6, np.nan, 3.8, 3.9, np.nan, 3.4, 3.6, 3.5, 
                          3.7, 3.8, np.nan, 3.9, 3.6, 3.5, 3.7, np.nan, 3.8, 3.9]
}

def main():
    """
    Función principal que ejecuta el análisis de salarios por ciudad.
    """
    
    print("EJERCICIO 1: IMPUTACIÓN POR MEDIA AGRUPADA POR CIUDAD")
    print("=" * 60)
    
    # 1. Crear DataFrame
    salarios_df = pd.DataFrame(salarios_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(salarios_df)
    print("_" * 40)
    print(f"Dimensiones: {salarios_df.shape}")
    
    # 2. Calcular medias por ciudad
    print("\n=== MEDIAS SALARIALES POR CIUDAD ===")
    medias = {}
    for ciudad in salarios_df.columns:
        media = salarios_df[ciudad].mean()
        medias[ciudad] = media
        nombre = ciudad.replace('salarios_', '').title()
        print(f"{nombre}: ${media:.3f}M")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medias
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    salarios_imputados = salarios_df.fillna(salarios_df.mean())
    
    for ciudad in salarios_df.columns:
        n_imputados = salarios_df[ciudad].isna().sum()
        nombre = ciudad.replace('salarios_', '').title()
        print(f"✓ {nombre}: {n_imputados} valores imputados con ${medias[ciudad]:.3f}M")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = salarios_imputados.round(3)
    datos_mostrar.columns = [col.replace('salarios_', '').title() for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)

    print(f"\nValores faltantes después de imputación: {salarios_imputados.isna().sum().sum()}")
    print("=" * 60)
    
    return salarios_imputados

if __name__ == "__main__":
    datos_final = main()
