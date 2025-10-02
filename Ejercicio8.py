"""
EJERCICIO 8: IMPUTACIÓN POR MEDIA AGRUPADA POR ESTACIÓN
=======================================================

Estudio de temperaturas promedio mensuales por estación meteorológica 
usando imputación por media para mantener la consistencia climática de cada ubicación.

"""

import numpy as np
import pandas as pd

# Datos de temperaturas promedio mensuales por estación (en °C)
temperaturas_ds = {
    "temperaturas_estacion_a": [22.5, 23.0, np.nan, 24.5, 23.5, 22.8, 23.2, np.nan, 24.0, 22.9, 
                                23.3, 23.7, np.nan, 22.6, 23.4, 23.8, 24.1, np.nan, 23.6, 23.9],
    "temperaturas_estacion_b": [18.0, 19.0, np.nan, 18.5, 19.2, 17.9, 18.7, np.nan, 19.1, 18.4, 
                                18.6, 18.9, np.nan, 18.3, 19.0, 18.8, 19.2, np.nan, 18.5, 19.1],
    "temperaturas_estacion_c": [25.0, 26.0, 27.0, 26.5, 25.5, 26.8, 27.2, np.nan, 25.9, 26.3, 
                                27.1, 26.7, np.nan, 25.8, 26.2, 26.9, 27.3, 25.7, 26.6, 27.0]
}

def main():
    """
    Función principal que ejecuta el análisis de temperaturas por estación meteorológica.
    """
    
    print("EJERCICIO 8: IMPUTACIÓN POR MEDIA AGRUPADA POR ESTACIÓN")
    print("=" * 55)
    
    # 1. Crear DataFrame
    temperaturas_df = pd.DataFrame(temperaturas_ds)
    
    print("\n=== DATOS ORIGINALES ===")
    print(temperaturas_df)
    print("_" * 40)
    print(f"Dimensiones: {temperaturas_df.shape}")
    
    # 2. Calcular medias por estación
    print("\n=== MEDIAS DE TEMPERATURA POR ESTACIÓN ===")
    medias = {}
    for estacion in temperaturas_df.columns:
        media = temperaturas_df[estacion].mean()
        medias[estacion] = media
        nombre = estacion.replace('temperaturas_', '').replace('_', ' ').title()
        print(f"{nombre}: {media:.2f}°C")
    print("_" * 40)
    
    # 3. Imputación usando fillna con medias
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    temperaturas_imputadas = temperaturas_df.copy()
    
    # Imputar cada columna con su respectiva media
    for estacion in temperaturas_df.columns:
        temperaturas_imputadas[estacion] = temperaturas_df[estacion].fillna(medias[estacion])
        n_imputados = temperaturas_df[estacion].isna().sum()
        nombre = estacion.replace('temperaturas_', '').replace('_', ' ').title()
        print(f"✓ {nombre}: {n_imputados} valores imputados con {medias[estacion]:.2f}°C")
    print("_" * 40)
    
    # 4. Datos finales imputados
    print("\n=== DATOS FINALES IMPUTADOS ===")
    datos_mostrar = temperaturas_imputadas.round(2)
    datos_mostrar.columns = [col.replace('temperaturas_', '').replace('_', ' ').title() for col in datos_mostrar.columns]
    print(datos_mostrar)
    print("_" * 40)
    
    print(f"\nValores faltantes después de imputación: {temperaturas_imputadas.isna().sum().sum()}")
    print("=" * 55)
    
    return temperaturas_imputadas

if __name__ == "__main__":
    datos_final = main()