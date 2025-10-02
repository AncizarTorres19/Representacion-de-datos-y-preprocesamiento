"""
Ejercicio 1 - Media por ciudad
Imputación de datos faltantes en salarios mensuales de trabajadores
en tres ciudades colombianas utilizando la media por ciudad.
"""

import pandas as pd
import numpy as np

def crear_datos_salarios():
    """
    Crea los datos de salarios con valores faltantes según el enunciado
    """
    # Datos de Bogotá (20 trabajadores)
    bogota = [2.5, 3.0, np.nan, 2.8, 3.1, 2.9, 3.3, np.nan, 2.7, 3.4, 
              3.0, np.nan, 2.6, 2.8, 3.2, 3.0, np.nan, 2.9, 3.1, 2.7]
    
    # Datos de Cali (20 trabajadores)
    cali = [1.8, 2.0, 2.1, np.nan, 1.9, 2.2, 2.3, 2.0, 1.7, np.nan, 
            2.1, 2.0, np.nan, 1.8, 2.4, 2.1, 2.2, 1.9, 2.0, np.nan]
    
    # Datos de Medellín (20 trabajadores)
    medellin = [3.5, 3.7, 3.6, np.nan, 3.8, 3.9, np.nan, 3.4, 3.6, 3.5, 
                3.7, 3.8, np.nan, 3.9, 3.6, 3.5, 3.7, np.nan, 3.8, 3.9]
    
    # Crear DataFrame
    datos = {
        'Ciudad': ['Bogotá'] * 20 + ['Cali'] * 20 + ['Medellín'] * 20,
        'Salario': bogota + cali + medellin
    }
    
    df = pd.DataFrame(datos)
    return df

def imputar_por_media_ciudad(df):
    """
    Imputa los valores faltantes utilizando la media salarial por ciudad
    """
    df_imputado = df.copy()
    
    # Calcular la media por ciudad (ignorando valores NaN)
    medias_ciudad = df.groupby('Ciudad')['Salario'].mean()
    
    print("=== MEDIAS SALARIALES POR CIUDAD ===")
    for ciudad, media in medias_ciudad.items():
        print(f"{ciudad}: {media:.3f} millones de pesos")
    
    # Imputar valores faltantes con la media de cada ciudad
    for ciudad in df['Ciudad'].unique():
        mascara_ciudad = df['Ciudad'] == ciudad
        mascara_nan = df['Salario'].isna()
        mascara_imputar = mascara_ciudad & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Salario'] = medias_ciudad[ciudad]
    
    return df_imputado, medias_ciudad

def mostrar_resultados(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for ciudad in df_original['Ciudad'].unique():
        datos_ciudad = df_original[df_original['Ciudad'] == ciudad]
        valores_faltantes = datos_ciudad['Salario'].isna().sum()
        total_registros = len(datos_ciudad)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\n{ciudad}:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for ciudad in df_original['Ciudad'].unique():
        print(f"\n{ciudad}:")
        
        # Datos originales
        datos_orig = df_original[df_original['Ciudad'] == ciudad]['Salario']
        datos_imput = df_imputado[df_imputado['Ciudad'] == ciudad]['Salario']
        
        print("  Datos originales:")
        valores_orig = [f"{x:.1f}" if not pd.isna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f"{x:.3f}" for x in datos_imput]
        print(f"    {valores_imput}")
    
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
    
    for ciudad in df_original['Ciudad'].unique():
        datos_orig = df_original[df_original['Ciudad'] == ciudad]['Salario']
        datos_imput = df_imputado[df_imputado['Ciudad'] == ciudad]['Salario']
        
        print(f"\n{ciudad}:")
        print(f"  Media original (sin NaN): {datos_orig.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Desviación estándar original: {datos_orig.std():.3f}")
        print(f"  Desviación estándar imputada: {datos_imput.std():.3f}")
        print(f"  Mediana: {datos_imput.median():.3f}")

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 1: IMPUTACIÓN POR MEDIA AGRUPADA POR CIUDAD")
    print("=" * 60)
    
    # Crear datos
    df_original = crear_datos_salarios()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Realizar imputación
    df_imputado, medias = imputar_por_media_ciudad(df_original)
    
    # Mostrar resultados detallados
    mostrar_resultados(df_original, df_imputado)
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Salario'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
