"""
EJERCICIO 3: IMPUTACIÓN POR MODA AGRUPADA POR GRUPO ETARIO
==========================================================

Estudio de comidas diarias por grupo etario usando imputación por moda
para preservar los patrones alimentarios típicos de cada grupo de edad.

"""

import numpy as np
import pandas as pd

# Datos de comidas diarias por grupo etario
comidas_ds = {
    "comidas_ninos": [4, 5, np.nan, 4, 5, 6, 4, np.nan, 5, 4, 
                      6, 5, np.nan, 4, 5, 6, 5, 4, np.nan, 5],
    "comidas_adultos_jovenes": [3, 4, 3, 4, np.nan, 3, 4, 3, 4, np.nan, 
                                3, 4, 3, 4, 3, 4, 3, np.nan, 4, 3],
    "comidas_adultos_medios": [3, 2, np.nan, 3, 2, 3, 2, 3, np.nan, 3, 
                               2, 3, 2, np.nan, 3, 2, 3, 2, 3, np.nan],
    "comidas_ancianos": [2, 2, np.nan, 3, 2, 2, 3, 2, np.nan, 2, 
                         3, 2, 2, np.nan, 3, 2, 2, 3, 2, np.nan]
}

def main():
    """
    Función principal que ejecuta el análisis de comidas diarias por grupo etario.
    """
    
    print("EJERCICIO 3: IMPUTACIÓN POR MODA AGRUPADA POR GRUPO ETARIO")
    print("=" * 60)
    
    # 1. Crear DataFrame
    comidas_df = pd.DataFrame(comidas_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(comidas_df)
    print("_" * 40)
    print(f"Dimensiones: {comidas_df.shape}")
    
    # 2. Calcular modas por grupo etario
    print("\n=== MODAS DE COMIDAS DIARIAS POR GRUPO ETARIO ===")
    modas = {}
    for grupo in comidas_df.columns:
        moda = comidas_df[grupo].mode()[0] if len(comidas_df[grupo].mode()) > 0 else comidas_df[grupo].median()
        modas[grupo] = moda
        nombre = grupo.replace('comidas_', '').replace('_', ' ').title()
        print(f"{nombre}: {moda:.0f} comidas diarias")
    print("_" * 40)
    
    # 3. Imputación usando fillna con modas
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    comidas_imputadas = comidas_df.copy()
    
    # Imputar cada columna con su respectiva moda
    for grupo in comidas_df.columns:
        comidas_imputadas[grupo] = comidas_df[grupo].fillna(modas[grupo])
        n_imputados = comidas_df[grupo].isna().sum()
        nombre = grupo.replace('comidas_', '').replace('_', ' ').title()
        print(f"✓ {nombre}: {n_imputados} valores imputados con {modas[grupo]:.0f} comidas")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = comidas_imputadas.round(0).astype(int)
    datos_mostrar.columns = [col.replace('comidas_', '').replace('_', ' ').title() for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {comidas_imputadas.isna().sum().sum()}")
    print("=" * 60)
    
    return comidas_imputadas

if __name__ == "__main__":
    datos_final = main()