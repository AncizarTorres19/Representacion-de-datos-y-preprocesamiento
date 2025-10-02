"""
EJERCICIO 7: IMPUTACIÓN POR MODA AGRUPADA POR GRUPO ETARIO
==========================================================

Estudio de nivel educativo por grupo etario usando imputación por moda
para preservar los patrones educativos predominantes de cada generación.

"""

import numpy as np
import pandas as pd

# Datos de nivel educativo por grupo etario
educacion_ds = {
    "educacion_18_30": ["Universitario", np.nan, "Técnico", "Universitario", "Secundaria", 
                        "Universitario", np.nan, "Técnico", "Universitario", "Primaria", 
                        "Técnico", np.nan, "Secundaria", "Universitario", "Universitario", 
                        "Técnico", np.nan, "Secundaria", "Universitario", "Técnico"],
    "educacion_31_50": ["Secundaria", "Universitario", np.nan, "Técnico", "Universitario", 
                        "Primaria", "Secundaria", "Universitario", "Universitario", np.nan, 
                        "Técnico", "Secundaria", "Universitario", np.nan, "Técnico", 
                        "Universitario", "Secundaria", "Universitario", "Primaria", np.nan],
    "educacion_51_mas": ["Primaria", "Secundaria", "Secundaria", np.nan, "Primaria", 
                         "Primaria", "Secundaria", "Primaria", "Primaria", "Secundaria", 
                         np.nan, "Primaria", "Primaria", "Secundaria", "Primaria", 
                         "Primaria", "Secundaria", np.nan, "Primaria", "Primaria"]
}

def main():
    """
    Función principal que ejecuta el análisis de nivel educativo por grupo etario.
    """
    
    print("EJERCICIO 7: IMPUTACIÓN POR MODA AGRUPADA POR GRUPO ETARIO")
    print("=" * 60)
    
    # 1. Crear DataFrame
    educacion_df = pd.DataFrame(educacion_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(educacion_df)
    print("_" * 40)
    print(f"Dimensiones: {educacion_df.shape}")
    
    # 2. Calcular modas por grupo etario
    print("\n=== MODAS DE NIVEL EDUCATIVO POR GRUPO ETARIO ===")
    modas = {}
    for grupo in educacion_df.columns:
        moda = educacion_df[grupo].mode()[0] if len(educacion_df[grupo].mode()) > 0 else "Secundaria"
        modas[grupo] = moda
        nombre = grupo.replace('educacion_', '').replace('_', '-') + ' años'
        print(f"{nombre}: {moda}")
    print("_" * 40)
    
    # 3. Imputación usando fillna con modas
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    educacion_imputada = educacion_df.copy()
    
    # Imputar cada columna con su respectiva moda
    for grupo in educacion_df.columns:
        educacion_imputada[grupo] = educacion_df[grupo].fillna(modas[grupo])
        n_imputados = educacion_df[grupo].isna().sum()
        nombre = grupo.replace('educacion_', '').replace('_', '-') + ' años'
        print(f"✓ {nombre}: {n_imputados} valores imputados con {modas[grupo]}")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = educacion_imputada.copy()
    datos_mostrar.columns = [col.replace('educacion_', '').replace('_', '-') + ' años' for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {educacion_imputada.isna().sum().sum()}")
    print("=" * 60)
    
    return educacion_imputada

if __name__ == "__main__":
    datos_final = main()