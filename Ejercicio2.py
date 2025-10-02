"""
Ejercicio 2 - Mediana por grado
Imputación de datos faltantes en horas de estudio semanales
en estudiantes de 6°, 7° y 8° grado utilizando la mediana por grado.
"""

import pandas as pd
import numpy as np

def crear_datos_estudio():
    """
    Crea los datos de horas de estudio con valores faltantes según el enunciado
    """
    # Datos de 6° grado (20 estudiantes)
    sexto = [5, 6, 7, np.nan, 8, 7, 6, np.nan, 5, 6, 
             7, 6, np.nan, 8, 7, 5, 6, np.nan, 7, 8]
    
    # Datos de 7° grado (20 estudiantes)
    septimo = [9, 8, 7, np.nan, 10, 9, 8, 7, 9, 10, 
               np.nan, 8, 9, 7, 10, 9, 8, 7, 10, np.nan]
    
    # Datos de 8° grado (20 estudiantes)
    octavo = [11, 12, 10, 11, np.nan, 12, 11, 10, 12, 11, 
              10, np.nan, 12, 11, 10, 12, np.nan, 11, 10, 12]
    
    # Crear DataFrame
    datos = {
        'Grado': ['6°'] * 20 + ['7°'] * 20 + ['8°'] * 20,
        'Horas_Estudio': sexto + septimo + octavo
    }
    
    df = pd.DataFrame(datos)
    return df

def imputar_por_mediana_grado(df):
    """
    Imputa los valores faltantes utilizando la mediana de horas de estudio por grado
    """
    df_imputado = df.copy()
    
    # Calcular la mediana por grado (ignorando valores NaN)
    medianas_grado = df.groupby('Grado')['Horas_Estudio'].median()
    
    print("=== MEDIANAS DE HORAS DE ESTUDIO POR GRADO ===")
    for grado, mediana in medianas_grado.items():
        print(f"{grado}: {mediana:.1f} horas semanales")
    
    # Imputar valores faltantes con la mediana de cada grado
    for grado in df['Grado'].unique():
        mascara_grado = df['Grado'] == grado
        mascara_nan = df['Horas_Estudio'].isna()
        mascara_imputar = mascara_grado & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Horas_Estudio'] = medianas_grado[grado]
    
    return df_imputado, medianas_grado

def analizar_robustez_mediana(df):
    """
    Analiza por qué la mediana es más robusta ante valores extremos
    """
    print("\n=== ANÁLISIS DE ROBUSTEZ DE LA MEDIANA ===")
    
    for grado in df['Grado'].unique():
        datos_grado = df[df['Grado'] == grado]['Horas_Estudio'].dropna()
        
        media = datos_grado.mean()
        mediana = datos_grado.median()
        desv_std = datos_grado.std()
        
        # Calcular cuartiles y rango intercuartílico
        q1 = datos_grado.quantile(0.25)
        q3 = datos_grado.quantile(0.75)
        iqr = q3 - q1
        
        # Identificar posibles valores extremos
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        outliers = datos_grado[(datos_grado < limite_inferior) | (datos_grado > limite_superior)]
        
        print(f"\n{grado}:")
        print(f"  Media: {media:.2f} horas")
        print(f"  Mediana: {mediana:.1f} horas")
        print(f"  Desviación estándar: {desv_std:.2f}")
        print(f"  Q1: {q1:.1f}, Q3: {q3:.1f}, IQR: {iqr:.1f}")
        print(f"  Rango de valores normales: [{limite_inferior:.1f}, {limite_superior:.1f}]")
        print(f"  Valores extremos detectados: {len(outliers)}")
        if len(outliers) > 0:
            print(f"    Valores: {list(outliers)}")

def mostrar_distribucion_datos(df):
    """
    Muestra la distribución de los datos por grado
    """
    print("\n=== DISTRIBUCIÓN DE DATOS POR GRADO ===")
    
    for grado in df['Grado'].unique():
        datos_grado = df[df['Grado'] == grado]['Horas_Estudio'].dropna()
        valores_unicos = datos_grado.value_counts().sort_index()
        
        print(f"\n{grado}:")
        print("  Distribución de frecuencias:")
        for valor, freq in valores_unicos.items():
            print(f"    {valor:.0f} horas: {freq} estudiantes")
        
        print(f"  Mínimo: {datos_grado.min():.0f} horas")
        print(f"  Máximo: {datos_grado.max():.0f} horas")
        print(f"  Rango: {datos_grado.max() - datos_grado.min():.0f} horas")

def mostrar_resultados(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for grado in df_original['Grado'].unique():
        datos_grado = df_original[df_original['Grado'] == grado]
        valores_faltantes = datos_grado['Horas_Estudio'].isna().sum()
        total_registros = len(datos_grado)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\n{grado}:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for grado in df_original['Grado'].unique():
        print(f"\n{grado}:")
        
        # Datos originales
        datos_orig = df_original[df_original['Grado'] == grado]['Horas_Estudio']
        datos_imput = df_imputado[df_imputado['Grado'] == grado]['Horas_Estudio']
        
        print("  Datos originales:")
        valores_orig = [f"{x:.0f}" if not pd.isna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f"{x:.1f}" for x in datos_imput]
        print(f"    {valores_imput}")
    
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS COMPARATIVAS ===")
    
    for grado in df_original['Grado'].unique():
        datos_orig = df_original[df_original['Grado'] == grado]['Horas_Estudio']
        datos_imput = df_imputado[df_imputado['Grado'] == grado]['Horas_Estudio']
        
        print(f"\n{grado}:")
        print(f"  Media original (sin NaN): {datos_orig.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Mediana original: {datos_orig.median():.1f}")
        print(f"  Mediana después de imputación: {datos_imput.median():.1f}")
        print(f"  Desviación estándar original: {datos_orig.std():.3f}")
        print(f"  Desviación estándar imputada: {datos_imput.std():.3f}")

def explicar_ventajas_mediana():
    """
    Explica las ventajas de usar mediana vs media para imputación
    """
    print("\n" + "="*70)
    print("VENTAJAS DE LA MEDIANA PARA IMPUTACIÓN")
    print("="*70)
    print("""
1. ROBUSTEZ ANTE VALORES EXTREMOS:
   - La mediana no se ve afectada por valores atípicos
   - La media sí es sensible a valores extremos
   
2. REPRESENTATIVIDAD:
   - La mediana representa el valor central de la distribución
   - Es menos influenciada por la forma de la distribución
   
3. ESTABILIDAD:
   - Pequeños cambios en los datos extremos no afectan la mediana
   - Proporciona una medida más estable del centro de los datos
   
4. INTERPRETACIÓN INTUITIVA:
   - 50% de los estudiantes estudian menos que la mediana
   - 50% de los estudiantes estudian más que la mediana
   
5. MEJOR PARA DATOS ORDINALES:
   - Las horas de estudio son datos cuantitativos ordinales
   - La mediana preserva mejor la naturaleza ordinal de los datos
    """)

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 2: IMPUTACIÓN POR MEDIANA AGRUPADA POR GRADO")
    print("=" * 65)
    
    # Crear datos
    df_original = crear_datos_estudio()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Mostrar distribución de datos
    mostrar_distribucion_datos(df_original)
    
    # Realizar imputación
    df_imputado, _ = imputar_por_mediana_grado(df_original)
    
    # Analizar robustez de la mediana
    analizar_robustez_mediana(df_original)
    
    # Mostrar resultados detallados
    mostrar_resultados(df_original, df_imputado)
    
    # Explicar ventajas de la mediana
    explicar_ventajas_mediana()
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Horas_Estudio'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
