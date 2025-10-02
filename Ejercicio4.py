"""
EJERCICIO 4: IMPUTACIÓN POR MEDIA AGRUPADA POR GRUPO ETARIO
===========================================================

Estudio de pasos diarios por grupo etario usando imputación por media
para preservar los patrones de actividad física típicos de cada grupo de edad.

"""

import numpy as np
import pandas as pd

# Datos de pasos diarios por grupo etario
pasos_ds = {
    "pasos_18_30": [7000, 7500, np.nan, 7200, 7600, 7400, 7300, 7500, np.nan, 7600, 
                    7200, 7400, 7300, 7500, np.nan, 7200, 7600, 7400, 7300, 7500],
    "pasos_31_50": [6000, 6500, np.nan, 6300, 6100, 6400, 6200, 6500, 6300, np.nan, 
                    6400, 6200, 6500, 6300, np.nan, 6100, 6400, 6200, 6500, 6300],
    "pasos_51_70": [4000, 4200, 4100, 3900, 4300, 4100, np.nan, 4200, 4000, 4300, 
                    4100, np.nan, 4200, 4000, 4300, 4100, np.nan, 4200, 4000, 4300]
}

def main():
    """
    Función principal que ejecuta el análisis de pasos diarios por grupo etario.
    """
    
    print("EJERCICIO 4: IMPUTACIÓN POR MEDIA AGRUPADA POR GRUPO ETARIO")
    print("=" * 60)
    
    # 1. Crear DataFrame
    pasos_df = pd.DataFrame(pasos_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(pasos_df)
    print("_" * 40)
    print(f"Dimensiones: {pasos_df.shape}")
    
    # 2. Calcular medias por grupo etario
    print("\n=== MEDIAS DE PASOS DIARIOS POR GRUPO ETARIO ===")
    medias = {}
    for grupo in pasos_df.columns:
        media = pasos_df[grupo].mean()
        medias[grupo] = media
        nombre = grupo.replace('pasos_', '').replace('_', '-') + ' años'
        print(f"{nombre}: {media:.0f} pasos diarios")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medias
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    pasos_imputados = pasos_df.copy()
    
    # Imputar cada columna con su respectiva media
    for grupo in pasos_df.columns:
        pasos_imputados[grupo] = pasos_df[grupo].fillna(medias[grupo])
        n_imputados = pasos_df[grupo].isna().sum()
        nombre = grupo.replace('pasos_', '').replace('_', '-') + ' años'
        print(f"✓ {nombre}: {n_imputados} valores imputados con {medias[grupo]:.0f} pasos")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = pasos_imputados.round(0).astype(int)
    datos_mostrar.columns = [col.replace('pasos_', '').replace('_', '-') + ' años' for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {pasos_imputados.isna().sum().sum()}")
    print("=" * 60)
    
    return pasos_imputados

if __name__ == "__main__":
    datos_final = main()