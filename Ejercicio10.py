"""
EJERCICIO 10: IMPUTACIÓN POR MEDIA AGRUPADA POR OPERADOR Y TURNO
================================================================

Estudio de call center con duración de llamadas por operador y turno usando imputación por media
para preservar los patrones de productividad específicos de cada operador en cada franja horaria.

"""

import numpy as np
import pandas as pd

# Datos de duración de llamadas por operador y turno (en minutos)
llamadas_ds = {
    "llamadas_operador_a_manana": [5, 6, np.nan, 7, 8, 6, 7, np.nan, 5, 7, 
                                   8, 6, 7, np.nan, 6, 8, 7, 5, 6, np.nan],
    "llamadas_operador_b_tarde": [8, 9, np.nan, 7, 8, 10, 9, np.nan, 8, 7, 
                                  9, 8, np.nan, 10, 9, 7, 8, 9, 8, 10],
    "llamadas_operador_c_noche": [10, 12, 11, np.nan, 9, 10, 12, 11, np.nan, 10, 
                                  11, 12, 10, 9, np.nan, 11, 12, 10, 9, 11]
}

def main():
    """
    Función principal que ejecuta el análisis de duración de llamadas por operador y turno.
    """
    
    print("EJERCICIO 10: IMPUTACIÓN POR MEDIA AGRUPADA POR OPERADOR Y TURNO")
    print("=" * 67)
    
    # 1. Crear DataFrame
    llamadas_df = pd.DataFrame(llamadas_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(llamadas_df)
    print("_" * 40)
    print(f"Dimensiones: {llamadas_df.shape}")
    
    # 2. Calcular medias por operador y turno
    print("\n=== MEDIAS DE DURACIÓN DE LLAMADAS POR OPERADOR Y TURNO ===")
    medias = {}
    for grupo in llamadas_df.columns:
        media = llamadas_df[grupo].mean()
        medias[grupo] = media
        nombre = grupo.replace('llamadas_', '').replace('_', ' ').title()
        print(f"{nombre}: {media:.2f} minutos")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medias
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    llamadas_imputadas = llamadas_df.copy()
    
    # Imputar cada columna con su respectiva media
    for grupo in llamadas_df.columns:
        llamadas_imputadas[grupo] = llamadas_df[grupo].fillna(medias[grupo])
        n_imputados = llamadas_df[grupo].isna().sum()
        nombre = grupo.replace('llamadas_', '').replace('_', ' ').title()
        print(f"✓ {nombre}: {n_imputados} valores imputados con {medias[grupo]:.2f} minutos")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = llamadas_imputadas.round(2)
    datos_mostrar.columns = [col.replace('llamadas_', '').replace('_', ' ').title() for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {llamadas_imputadas.isna().sum().sum()}")
    print("=" * 67)
    
    return llamadas_imputadas

if __name__ == "__main__":
    datos_final = main()