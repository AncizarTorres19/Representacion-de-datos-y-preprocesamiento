"""
Ejercicio 3 - Moda por grupo etario
Imputación de datos faltantes en número de comidas diarias
por grupo etario utilizando la moda por grupo.
"""

import pandas as pd
import numpy as np

def crear_datos_comidas():
    """
    Crea los datos de número de comidas diarias con valores faltantes según el enunciado
    """
    # Datos de Niños (20 registros)
    ninos = [4, 5, np.nan, 4, 5, 6, 4, np.nan, 5, 4, 
             6, 5, np.nan, 4, 5, 6, 5, 4, np.nan, 5]
    
    # Datos de Adultos jóvenes (20 registros)
    adultos_jovenes = [3, 4, 3, 4, np.nan, 3, 4, 3, 4, np.nan, 
                       3, 4, 3, 4, 3, 4, 3, np.nan, 4, 3]
    
    # Datos de Adultos medios (20 registros)
    adultos_medios = [3, 2, np.nan, 3, 2, 3, 2, 3, np.nan, 3, 
                      2, 3, 2, np.nan, 3, 2, 3, 2, 3, np.nan]
    
    # Datos de Ancianos (20 registros)
    ancianos = [2, 2, np.nan, 3, 2, 2, 3, 2, np.nan, 2, 
                3, 2, 2, np.nan, 3, 2, 2, 3, 2, np.nan]
    
    # Crear DataFrame
    datos = {
        'Grupo_Etario': ['Niños'] * 20 + ['Adultos_Jóvenes'] * 20 + 
                       ['Adultos_Medios'] * 20 + ['Ancianos'] * 20,
        'Comidas_Diarias': ninos + adultos_jovenes + adultos_medios + ancianos
    }
    
    df = pd.DataFrame(datos)
    return df

def calcular_moda_grupo(serie):
    """
    Calcula la moda de una serie, manejando casos especiales
    """
    serie_limpia = serie.dropna()
    if len(serie_limpia) == 0:
        return np.nan, 0
    
    # Usar pandas para calcular la moda
    frecuencias = serie_limpia.value_counts()
    if len(frecuencias) == 0:
        return np.nan, 0
    
    moda_valor = frecuencias.index[0]  # El valor más frecuente
    moda_frecuencia = frecuencias.iloc[0]  # Su frecuencia
    
    return moda_valor, moda_frecuencia

def imputar_por_moda_grupo(df):
    """
    Imputa los valores faltantes utilizando la moda del número de comidas por grupo etario
    """
    df_imputado = df.copy()
    
    # Calcular la moda por grupo etario
    modas_grupo = {}
    frecuencias_moda = {}
    
    print("=== MODAS DE COMIDAS DIARIAS POR GRUPO ETARIO ===")
    
    for grupo in df['Grupo_Etario'].unique():
        datos_grupo = df[df['Grupo_Etario'] == grupo]['Comidas_Diarias']
        moda_valor, moda_frecuencia = calcular_moda_grupo(datos_grupo)
        
        modas_grupo[grupo] = moda_valor
        frecuencias_moda[grupo] = moda_frecuencia
        
        total_validos = datos_grupo.count()
        porcentaje_moda = (moda_frecuencia / total_validos) * 100
        
        print(f"{grupo}: {moda_valor:.0f} comidas/día (frecuencia: {moda_frecuencia}/{total_validos}, {porcentaje_moda:.1f}%)")
    
    # Imputar valores faltantes con la moda de cada grupo
    for grupo in df['Grupo_Etario'].unique():
        mascara_grupo = df['Grupo_Etario'] == grupo
        mascara_nan = df['Comidas_Diarias'].isna()
        mascara_imputar = mascara_grupo & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Comidas_Diarias'] = modas_grupo[grupo]
    
    return df_imputado, modas_grupo, frecuencias_moda

def analizar_distribucion_frecuencias(df):
    """
    Analiza la distribución de frecuencias por grupo etario
    """
    print("\n=== ANÁLISIS DE DISTRIBUCIÓN DE FRECUENCIAS ===")
    
    for grupo in df['Grupo_Etario'].unique():
        datos_grupo = df[df['Grupo_Etario'] == grupo]['Comidas_Diarias'].dropna()
        
        print(f"\n{grupo}:")
        
        # Calcular frecuencias
        frecuencias = datos_grupo.value_counts().sort_index()
        total = len(datos_grupo)
        
        print("  Distribución completa:")
        for valor, freq in frecuencias.items():
            porcentaje = (freq / total) * 100
            print(f"    {valor:.0f} comidas: {freq} personas ({porcentaje:.1f}%)")
        
        # Estadísticas adicionales
        print(f"  Total de registros válidos: {total}")
        print(f"  Rango: {datos_grupo.min():.0f} - {datos_grupo.max():.0f} comidas")
        print(f"  Media: {datos_grupo.mean():.2f} comidas")
        print(f"  Mediana: {datos_grupo.median():.1f} comidas")

def verificar_multimodalidad(df):
    """
    Verifica si existen casos de multimodalidad en los datos
    """
    print("\n=== VERIFICACIÓN DE MULTIMODALIDAD ===")
    
    for grupo in df['Grupo_Etario'].unique():
        datos_grupo = df[df['Grupo_Etario'] == grupo]['Comidas_Diarias'].dropna()
        frecuencias = datos_grupo.value_counts()
        max_frecuencia = frecuencias.max()
        
        # Encontrar todos los valores con la frecuencia máxima
        modas = frecuencias[frecuencias == max_frecuencia].index.tolist()
        
        print(f"\n{grupo}:")
        if len(modas) == 1:
            print(f"  ✓ Unimodal: {modas[0]:.0f} comidas (frecuencia: {max_frecuencia})")
        else:
            print(f"  ⚠ Multimodal: {[f'{m:.0f}' for m in modas]} comidas (frecuencia: {max_frecuencia} cada una)")
            print("    En caso multimodal, se selecciona el primer valor ordenado")

def mostrar_resultados(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for grupo in df_original['Grupo_Etario'].unique():
        datos_grupo = df_original[df_original['Grupo_Etario'] == grupo]
        valores_faltantes = datos_grupo['Comidas_Diarias'].isna().sum()
        total_registros = len(datos_grupo)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\n{grupo}:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for grupo in df_original['Grupo_Etario'].unique():
        print(f"\n{grupo}:")
        
        # Datos originales
        datos_orig = df_original[df_original['Grupo_Etario'] == grupo]['Comidas_Diarias']
        datos_imput = df_imputado[df_imputado['Grupo_Etario'] == grupo]['Comidas_Diarias']
        
        print("  Datos originales:")
        valores_orig = [f"{x:.0f}" if not pd.isna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f"{x:.0f}" for x in datos_imput]
        print(f"    {valores_imput}")
    
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS COMPARATIVAS ===")
    
    for grupo in df_original['Grupo_Etario'].unique():
        datos_orig = df_original[df_original['Grupo_Etario'] == grupo]['Comidas_Diarias']
        datos_imput = df_imputado[df_imputado['Grupo_Etario'] == grupo]['Comidas_Diarias']
        
        print(f"\n{grupo}:")
        print(f"  Media original (sin NaN): {datos_orig.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Mediana original: {datos_orig.median():.1f}")
        print(f"  Mediana después de imputación: {datos_imput.median():.1f}")
        
        # Calcular moda antes y después usando pandas
        moda_orig = datos_orig.dropna().mode()
        moda_imput = datos_imput.mode()
        
        moda_orig_val = moda_orig.iloc[0] if len(moda_orig) > 0 else np.nan
        moda_imput_val = moda_imput.iloc[0] if len(moda_imput) > 0 else np.nan
        
        print(f"  Moda original: {moda_orig_val:.0f}")
        print(f"  Moda después de imputación: {moda_imput_val:.0f}")

def explicar_ventajas_moda():
    """
    Explica las ventajas de usar moda para variables categóricas/discretas
    """
    print("\n" + "="*70)
    print("VENTAJAS DE LA MODA PARA IMPUTACIÓN DE VARIABLES DISCRETAS")
    print("="*70)
    print("""
1. ADECUADA PARA VARIABLES CATEGÓRICAS/DISCRETAS:
   - El número de comidas es una variable discreta con valores limitados
   - La moda preserva la naturaleza categórica de los datos
   
2. REPRESENTA EL VALOR MÁS COMÚN:
   - Refleja el comportamiento más típico del grupo
   - Es especialmente útil cuando hay patrones claros de comportamiento
   
3. NO INTRODUCE VALORES IRREALES:
   - Solo usa valores que realmente existen en los datos
   - No genera números decimales o intermedios sin sentido
   
4. ROBUSTA ANTE DISTRIBUCIONES ASIMÉTRICAS:
   - No se ve afectada por la forma de la distribución
   - Funciona bien con distribuciones sesgadas
   
5. INTERPRETACIÓN DIRECTA:
   - Fácil de entender: "el valor más frecuente en el grupo"
   - Relevante para variables de comportamiento y hábitos
   
6. PRESERVA LA ESTRUCTURA DE LOS DATOS:
   - Mantiene las proporciones originales de cada categoría
   - No altera significativamente la distribución original

CASOS ESPECIALES:
- Multimodalidad: Cuando hay empate, se puede usar criterios adicionales
- Distribución uniforme: Cuando todos los valores tienen igual frecuencia
    """)

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 3: IMPUTACIÓN POR MODA AGRUPADA POR GRUPO ETARIO")
    print("=" * 70)
    
    # Crear datos
    df_original = crear_datos_comidas()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Analizar distribución de frecuencias
    analizar_distribucion_frecuencias(df_original)
    
    # Verificar multimodalidad
    verificar_multimodalidad(df_original)
    
    # Realizar imputación
    df_imputado, _, _ = imputar_por_moda_grupo(df_original)
    
    # Mostrar resultados detallados
    mostrar_resultados(df_original, df_imputado)
    
    # Explicar ventajas de la moda
    explicar_ventajas_moda()
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Comidas_Diarias'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    # Resumen final por grupo
    print("\n=== RESUMEN FINAL POR GRUPO ETARIO ===")
    for grupo in df_imputado['Grupo_Etario'].unique():
        datos_grupo = df_imputado[df_imputado['Grupo_Etario'] == grupo]['Comidas_Diarias']
        frecuencias_final = datos_grupo.value_counts().sort_index()
        
        print(f"\n{grupo}:")
        for valor, freq in frecuencias_final.items():
            porcentaje = (freq / len(datos_grupo)) * 100
            print(f"  {valor:.0f} comidas: {freq} personas ({porcentaje:.1f}%)")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
