"""
EJERCICIO 6: IMPUTACIÓN POR MEDIANA AGRUPADA POR REGIÓN
=======================================================

Estudio de tamaños de parcelas agrícolas por región usando imputación por mediana
para manejar la dispersión y posibles valores atípicos en datos agrícolas.

"""

import numpy as np
import pandas as pd

# Datos de tamaños de parcelas agrícolas por región (en hectáreas)
parcelas_ds = {
    "parcelas_llanos": [50, 60, np.nan, 55, 70, 65, 62, 59, np.nan, 54, 
                        66, 63, 68, np.nan, 57, 61, 64, 58, 67, 69],
    "parcelas_andina": [20, 25, 28, np.nan, 22, 30, 27, 24, 26, np.nan, 
                        29, 23, 21, np.nan, 22, 24, 25, 27, 28, 23],
    "parcelas_caribe": [15, 18, 17, np.nan, 16, 19, 20, 21, np.nan, 22, 
                        18, 16, 19, np.nan, 20, 17, 18, 19, 21, np.nan]
}

def main():
    """
    Función principal que ejecuta el análisis de parcelas agrícolas por región.
    """
    
    print("EJERCICIO 6: IMPUTACIÓN POR MEDIANA AGRUPADA POR REGIÓN")
    print("=" * 57)
    
    # 1. Crear DataFrame
    parcelas_df = pd.DataFrame(parcelas_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(parcelas_df)
    print("_" * 40)
    print(f"Dimensiones: {parcelas_df.shape}")
    
    # 2. Calcular medianas por región
    print("\n=== MEDIANAS DE TAMAÑO DE PARCELAS POR REGIÓN ===")
    medianas = {}
    for region in parcelas_df.columns:
        mediana = parcelas_df[region].median()
        medianas[region] = mediana
        nombre = region.replace('parcelas_', '').title()
        print(f"Región {nombre}: {mediana:.1f} hectáreas")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medianas
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    parcelas_imputadas = parcelas_df.copy()
    
    # Imputar cada columna con su respectiva mediana
    for region in parcelas_df.columns:
        parcelas_imputadas[region] = parcelas_df[region].fillna(medianas[region])
        n_imputados = parcelas_df[region].isna().sum()
        nombre = region.replace('parcelas_', '').title()
        print(f"✓ Región {nombre}: {n_imputados} valores imputados con {medianas[region]:.1f} hectáreas")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = parcelas_imputadas.round(1)
    datos_mostrar.columns = [col.replace('parcelas_', '').title() for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {parcelas_imputadas.isna().sum().sum()}")
    print("=" * 57)
    
    return parcelas_imputadas

if __name__ == "__main__":
    datos_final = main()