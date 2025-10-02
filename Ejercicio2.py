"""
EJERCICIO 2: IMPUTACIÓN POR MEDIANA AGRUPADA POR GRADO
======================================================

Estudio de horas de estudio semanales por grado usando imputación por mediana
para manejar la robustez ante valores extremos en cada nivel académico.

"""

import numpy as np
import pandas as pd

# Datos de horas de estudio por grado (horas semanales)
horas_ds = {
    "horas_sexto": [5, 6, 7, np.nan, 8, 7, 6, np.nan, 5, 6, 
                    7, 6, np.nan, 8, 7, 5, 6, np.nan, 7, 8],
    "horas_septimo": [9, 8, 7, np.nan, 10, 9, 8, 7, 9, 10, 
                      np.nan, 8, 9, 7, 10, 9, 8, 7, 10, np.nan],
    "horas_octavo": [11, 12, 10, 11, np.nan, 12, 11, 10, 12, 11, 
                     10, np.nan, 12, 11, 10, 12, np.nan, 11, 10, 12]
}

def main():
    """
    Función principal que ejecuta el análisis de horas de estudio por grado.
    """
    
    print("EJERCICIO 2: IMPUTACIÓN POR MEDIANA AGRUPADA POR GRADO")
    print("=" * 60)
    
    # 1. Crear DataFrame
    horas_df = pd.DataFrame(horas_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(horas_df)
    print("_" * 40)
    print(f"Dimensiones: {horas_df.shape}")
    
    # 2. Calcular medianas por grado
    print("\n=== MEDIANAS DE HORAS DE ESTUDIO POR GRADO ===")
    medianas = {}
    for grado in horas_df.columns:
        mediana = horas_df[grado].median()
        medianas[grado] = mediana
        nombre = grado.replace('horas_', '').replace('sexto', '6°').replace('septimo', '7°').replace('octavo', '8°')
        print(f"{nombre}: {mediana:.1f} horas semanales")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medianas
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    horas_imputadas = horas_df.fillna(horas_df.median())
    
    for grado in horas_df.columns:
        n_imputados = horas_df[grado].isna().sum()
        nombre = grado.replace('horas_', '').replace('sexto', '6°').replace('septimo', '7°').replace('octavo', '8°')
        print(f"✓ {nombre}: {n_imputados} valores imputados con {medianas[grado]:.1f} horas")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = horas_imputadas.round(1)
    datos_mostrar.columns = [col.replace('horas_', '').replace('sexto', '6°').replace('septimo', '7°').replace('octavo', '8°') for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {horas_imputadas.isna().sum().sum()}")
    print("=" * 60)
    
    return horas_imputadas

if __name__ == "__main__":
    datos_final = main()