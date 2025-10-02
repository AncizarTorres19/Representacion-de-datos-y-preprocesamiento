"""
EJERCICIO 9: IMPUTACIÓN POR MEDIA AGRUPADA POR GRUPO DEMOGRÁFICO
================================================================

Estudio nutricional de peso corporal por sexo y rango etario usando imputación por media
para preservar los perfiles antropométricos característicos de cada subgrupo demográfico.

"""

import numpy as np
import pandas as pd

# Datos de peso corporal por grupo demográfico (en kg)
pesos_ds = {
    "pesos_mujeres_jovenes": [55, np.nan, 60, 58, 56, 57, np.nan, 59, 61, 62, 
                              54, 55, np.nan, 60, 58, 57, 59, np.nan, 61, 56],
    "pesos_hombres_jovenes": [70, 75, np.nan, 72, 71, 74, 76, np.nan, 73, 72, 
                              70, 71, np.nan, 74, 76, 75, 73, np.nan, 72, 70],
    "pesos_adultos_mayores": [68, 72, 70, 71, np.nan, 73, 69, 72, 70, 71, 
                              np.nan, 68, 70, 72, 69, 71, np.nan, 70, 72, 71]
}

def main():
    """
    Función principal que ejecuta el análisis de peso corporal por grupo demográfico.
    """
    
    print("EJERCICIO 9: IMPUTACIÓN POR MEDIA AGRUPADA POR GRUPO DEMOGRÁFICO")
    print("=" * 66)
    
    # 1. Crear DataFrame
    pesos_df = pd.DataFrame(pesos_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(pesos_df)
    print("_" * 40)
    print(f"Dimensiones: {pesos_df.shape}")
    
    # 2. Calcular medias por grupo demográfico
    print("\n=== MEDIAS DE PESO CORPORAL POR GRUPO DEMOGRÁFICO ===")
    medias = {}
    for grupo in pesos_df.columns:
        media = pesos_df[grupo].mean()
        medias[grupo] = media
        nombre = grupo.replace('pesos_', '').replace('_', ' ').title()
        print(f"{nombre}: {media:.2f} kg")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medias
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    pesos_imputados = pesos_df.copy()
    
    # Imputar cada columna con su respectiva media
    for grupo in pesos_df.columns:
        pesos_imputados[grupo] = pesos_df[grupo].fillna(medias[grupo])
        n_imputados = pesos_df[grupo].isna().sum()
        nombre = grupo.replace('pesos_', '').replace('_', ' ').title()
        print(f"✓ {nombre}: {n_imputados} valores imputados con {medias[grupo]:.2f} kg")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = pesos_imputados.round(2)
    datos_mostrar.columns = [col.replace('pesos_', '').replace('_', ' ').title() for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {pesos_imputados.isna().sum().sum()}")
    print("=" * 66)
    
    return pesos_imputados

if __name__ == "__main__":
    datos_final = main()