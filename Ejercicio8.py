"""
Ejercicio 8 - Media por estación
Imputación de datos faltantes en temperaturas promedio mensuales
de sistema meteorológico utilizando la media por estación.
"""

import pandas as pd
import numpy as np

def crear_datos_temperaturas():
    """
    Crea los datos de temperaturas con valores faltantes según el enunciado
    """
    # Datos de la Estación A (20 registros)
    estacion_a = [22.5, 23.0, np.nan, 24.5, 23.5, 22.8, 23.2, np.nan, 24.0, 22.9, 
                  23.3, 23.7, np.nan, 22.6, 23.4, 23.8, 24.1, np.nan, 23.6, 23.9]
    
    # Datos de la Estación B (20 registros)
    estacion_b = [18.0, 19.0, np.nan, 18.5, 19.2, 17.9, 18.7, np.nan, 19.1, 18.4, 
                  18.6, 18.9, np.nan, 18.3, 19.0, 18.8, 19.2, np.nan, 18.5, 19.1]
    
    # Datos de la Estación C (20 registros)
    estacion_c = [25.0, 26.0, 27.0, 26.5, 25.5, 26.8, 27.2, np.nan, 25.9, 26.3, 
                  27.1, 26.7, np.nan, 25.8, 26.2, 26.9, 27.3, 25.7, 26.6, 27.0]
    
    # Crear DataFrame con números de mes
    datos = {
        'Estacion': ['Estación A'] * 20 + ['Estación B'] * 20 + ['Estación C'] * 20,
        'Mes': list(range(1, 21)) * 3,  # Meses 1-20 para cada estación
        'Temperatura': estacion_a + estacion_b + estacion_c
    }
    
    df = pd.DataFrame(datos)
    return df

def imputar_por_media_estacion(df):
    """
    Imputa los valores faltantes utilizando la media de temperatura por estación
    """
    df_imputado = df.copy()
    
    # Calcular la media por estación (ignorando valores NaN)
    medias_estacion = df.groupby('Estacion')['Temperatura'].mean()
    
    print("=== MEDIAS DE TEMPERATURA POR ESTACIÓN ===")
    for estacion, media in medias_estacion.items():
        print(f"{estacion}: {media:.3f}°C")
    
    # Imputar valores faltantes con la media de cada estación
    for estacion in df['Estacion'].unique():
        mascara_estacion = df['Estacion'] == estacion
        mascara_nan = df['Temperatura'].isna()
        mascara_imputar = mascara_estacion & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Temperatura'] = medias_estacion[estacion]
    
    return df_imputado, medias_estacion

def analizar_datos_meteorologicos(df):
    """
    Analiza las características meteorológicas de cada estación
    """
    print("\n=== ANÁLISIS METEOROLÓGICO POR ESTACIÓN ===")
    
    for estacion in df['Estacion'].unique():
        datos_estacion = df[df['Estacion'] == estacion]['Temperatura'].dropna()
        
        # Estadísticas descriptivas
        media = datos_estacion.mean()
        mediana = datos_estacion.median()
        desv_std = datos_estacion.std()
        temp_min = datos_estacion.min()
        temp_max = datos_estacion.max()
        rango = temp_max - temp_min
        
        # Coeficiente de variación
        cv = (desv_std / media) * 100
        
        # Cuartiles
        q1 = datos_estacion.quantile(0.25)
        q3 = datos_estacion.quantile(0.75)
        
        print(f"\n{estacion}:")
        print(f"  Media: {media:.3f}°C")
        print(f"  Mediana: {mediana:.3f}°C")
        print(f"  Desviación estándar: {desv_std:.3f}°C")
        print(f"  Coeficiente de variación: {cv:.2f}%")
        print(f"  Temperatura mínima: {temp_min:.1f}°C")
        print(f"  Temperatura máxima: {temp_max:.1f}°C")
        print(f"  Rango térmico: {rango:.1f}°C")
        print(f"  Q1: {q1:.1f}°C, Q3: {q3:.1f}°C")
        
        # Clasificación climática aproximada
        if media < 15:
            clima = "Frío"
        elif media < 20:
            clima = "Templado frío"
        elif media < 25:
            clima = "Templado"
        else:
            clima = "Cálido"
        
        print(f"  Clasificación climática: {clima}")

def validar_consistencia_temporal(df):
    """
    Valida la consistencia temporal de los datos
    """
    print("\n=== VALIDACIÓN DE CONSISTENCIA TEMPORAL ===")
    
    for estacion in df['Estacion'].unique():
        datos_estacion = df[df['Estacion'] == estacion]
        temperaturas = datos_estacion['Temperatura'].dropna()
        
        # Calcular diferencias consecutivas
        diferencias = temperaturas.diff().dropna()
        max_diferencia = diferencias.abs().max()
        diferencia_promedio = diferencias.abs().mean()
        
        # Detectar cambios bruscos (más de 2 desviaciones estándar)
        limite_cambio = 2 * temperaturas.std()
        cambios_bruscos = diferencias[diferencias.abs() > limite_cambio]
        
        print(f"\n{estacion}:")
        print(f"  Diferencia máxima consecutiva: {max_diferencia:.2f}°C")
        print(f"  Diferencia promedio consecutiva: {diferencia_promedio:.2f}°C")
        print(f"  Cambios bruscos detectados: {len(cambios_bruscos)}")
        
        if len(cambios_bruscos) > 0:
            print(f"    Valores: {list(cambios_bruscos.round(2))}")
        
        # Evaluación de estabilidad
        if cv := (temperaturas.std() / temperaturas.mean()) * 100:
            if cv < 5:
                estabilidad = "Muy estable"
            elif cv < 10:
                estabilidad = "Estable"
            elif cv < 15:
                estabilidad = "Moderadamente variable"
            else:
                estabilidad = "Muy variable"
            
            print(f"  Estabilidad térmica: {estabilidad} (CV: {cv:.2f}%)")

def analizar_patrones_estacionales(df):
    """
    Analiza posibles patrones estacionales en los datos
    """
    print("\n=== ANÁLISIS DE PATRONES ESTACIONALES ===")
    
    for estacion in df['Estacion'].unique():
        datos_estacion = df[df['Estacion'] == estacion]
        
        # Agrupar por trimestres (asumiendo que los meses 1-20 representan datos secuenciales)
        datos_estacion = datos_estacion.copy()
        datos_estacion['Trimestre'] = pd.cut(datos_estacion['Mes'], 
                                           bins=[0, 5, 10, 15, 20], 
                                           labels=['T1 (1-5)', 'T2 (6-10)', 'T3 (11-15)', 'T4 (16-20)'])
        
        # Calcular estadísticas por trimestre
        stats_trimestre = datos_estacion.groupby('Trimestre')['Temperatura'].agg(['mean', 'std', 'count']).round(2)
        
        print(f"\n{estacion} - Análisis por períodos:")
        print(stats_trimestre)
        
        # Identificar período más cálido y más frío
        temperaturas_validas = datos_estacion['Temperatura'].dropna()
        if len(temperaturas_validas) > 0:
            temp_max_idx = temperaturas_validas.idxmax()
            temp_min_idx = temperaturas_validas.idxmin()
            
            mes_max = datos_estacion.loc[temp_max_idx, 'Mes']
            mes_min = datos_estacion.loc[temp_min_idx, 'Mes']
            temp_max = temperaturas_validas.max()
            temp_min = temperaturas_validas.min()
            
            print(f"  Temperatura máxima: {temp_max:.1f}°C (Mes {mes_max})")
            print(f"  Temperatura mínima: {temp_min:.1f}°C (Mes {mes_min})")

def comparar_estaciones_climaticas(df):
    """
    Compara las características climáticas entre estaciones
    """
    print("\n=== COMPARACIÓN ENTRE ESTACIONES CLIMÁTICAS ===")
    
    # Crear resumen comparativo
    resumen = df.groupby('Estacion')['Temperatura'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(3)
    
    print("\nResumen estadístico comparativo:")
    print(resumen)
    
    # Ranking térmico
    medias_ordenadas = df.groupby('Estacion')['Temperatura'].mean().sort_values(ascending=False)
    
    print("\nRanking térmico (de mayor a menor temperatura):")
    for i, (estacion, media) in enumerate(medias_ordenadas.items(), 1):
        print(f"  {i}. {estacion}: {media:.3f}°C")
    
    # Análisis de variabilidad
    print("\nAnálisis de variabilidad (menor CV = más estable):")
    for estacion in df['Estacion'].unique():
        datos = df[df['Estacion'] == estacion]['Temperatura'].dropna()
        cv = (datos.std() / datos.mean()) * 100
        print(f"  {estacion}: CV = {cv:.2f}%")
    
    # Diferencias entre estaciones
    print("\nDiferencias térmicas entre estaciones:")
    estaciones = list(medias_ordenadas.index)
    for i in range(len(estaciones)):
        for j in range(i+1, len(estaciones)):
            est1, est2 = estaciones[i], estaciones[j]
            diff = medias_ordenadas[est1] - medias_ordenadas[est2]
            print(f"  {est1} vs {est2}: {diff:.3f}°C de diferencia")

def validar_calidad_datos_meteorologicos(df):
    """
    Valida la calidad de los datos meteorológicos
    """
    print("\n=== VALIDACIÓN DE CALIDAD DE DATOS METEOROLÓGICOS ===")
    
    for estacion in df['Estacion'].unique():
        datos_estacion = df[df['Estacion'] == estacion]['Temperatura']
        
        # Análisis de valores extremos
        q1 = datos_estacion.quantile(0.25)
        q3 = datos_estacion.quantile(0.75)
        iqr = q3 - q1
        
        limite_inf = q1 - 1.5 * iqr
        limite_sup = q3 + 1.5 * iqr
        
        outliers = datos_estacion[(datos_estacion < limite_inf) | (datos_estacion > limite_sup)]
        
        # Análisis de rango físicamente plausible
        temp_min_plausible = -50  # °C
        temp_max_plausible = 60   # °C
        
        valores_implausibles = datos_estacion[
            (datos_estacion < temp_min_plausible) | (datos_estacion > temp_max_plausible)
        ].dropna()
        
        print(f"\n{estacion}:")
        print(f"  Valores atípicos estadísticos: {len(outliers)}")
        if len(outliers) > 0:
            print(f"    Valores: {list(outliers.dropna().round(2))}")
        
        print(f"  Valores físicamente implausibles: {len(valores_implausibles)}")
        if len(valores_implausibles) > 0:
            print(f"    Valores: {list(valores_implausibles.round(2))}")
        
        # Evaluación general de calidad
        total_datos = len(datos_estacion)
        datos_validos = datos_estacion.count()
        completitud = (datos_validos / total_datos) * 100
        
        print(f"  Completitud de datos: {completitud:.1f}% ({datos_validos}/{total_datos})")
        
        if completitud >= 90:
            calidad = "Excelente"
        elif completitud >= 80:
            calidad = "Buena"
        elif completitud >= 70:
            calidad = "Regular"
        else:
            calidad = "Deficiente"
        
        print(f"  Calidad general: {calidad}")

def mostrar_resultados_imputacion(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for estacion in df_original['Estacion'].unique():
        datos_estacion = df_original[df_original['Estacion'] == estacion]
        valores_faltantes = datos_estacion['Temperatura'].isna().sum()
        total_registros = len(datos_estacion)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\n{estacion}:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for estacion in df_original['Estacion'].unique():
        print(f"\n{estacion}:")
        
        # Datos originales y imputados
        datos_orig = df_original[df_original['Estacion'] == estacion]['Temperatura']
        datos_imput = df_imputado[df_imputado['Estacion'] == estacion]['Temperatura']
        
        print("  Datos originales:")
        valores_orig = [f"{x:.1f}" if not pd.isna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f"{x:.3f}" for x in datos_imput]
        print(f"    {valores_imput}")
    
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS COMPARATIVAS ===")
    
    for estacion in df_original['Estacion'].unique():
        datos_orig = df_original[df_original['Estacion'] == estacion]['Temperatura']
        datos_imput = df_imputado[df_imputado['Estacion'] == estacion]['Temperatura']
        
        print(f"\n{estacion}:")
        print(f"  Media original (sin NaN): {datos_orig.mean():.6f}")
        print(f"  Media después de imputación: {datos_imput.mean():.6f}")
        print(f"  Mediana original: {datos_orig.median():.3f}")
        print(f"  Mediana después de imputación: {datos_imput.median():.3f}")
        print(f"  Desviación estándar original: {datos_orig.std():.6f}")
        print(f"  Desviación estándar imputada: {datos_imput.std():.6f}")

def explicar_ventajas_media_meteorologica():
    """
    Explica las ventajas específicas de usar media para datos meteorológicos
    """
    print("\n" + "="*80)
    print("VENTAJAS DE LA MEDIA PARA DATOS METEOROLÓGICOS")
    print("="*80)
    print("""
1. ADECUADA PARA VARIABLES CONTINUAS:
   - Las temperaturas son variables continuas con distribución aproximadamente normal
   - La media utiliza toda la información disponible de los datos
   - Proporciona el valor central más representativo
   
2. CONSERVACIÓN DE PROPIEDADES FÍSICAS:
   - Preserva las características térmicas de cada estación
   - Mantiene la coherencia con las leyes físicas de transferencia de calor
   - Respeta los gradientes térmicos naturales entre estaciones
   
3. ESTABILIDAD TEMPORAL:
   - Las temperaturas promedio mensuales tienden a ser estables
   - Pocos valores extremos que distorsionen la media
   - Apropiada para series temporales meteorológicas
   
4. COMPATIBILIDAD CON MODELOS CLIMÁTICOS:
   - Base estándar para cálculos climatológicos
   - Compatible con análisis de tendencias y proyecciones
   - Coherente con métodos de interpolación espacial
   
5. INTERPRETACIÓN METEOROLÓGICA:
   - Representa la temperatura característica de la estación
   - Útil para clasificaciones climáticas
   - Base para análisis de anomalías térmicas
   
6. MINIMIZACIÓN DE ERROR:
   - Minimiza la suma de cuadrados de las desviaciones
   - Óptima desde el punto de vista estadístico
   - Reduce el error de estimación en modelos predictivos

APLICACIONES ESPECÍFICAS:
- Relleno de series meteorológicas
- Análisis de cambio climático
- Modelos de predicción térmica
- Estudios de variabilidad climática
- Normalización de datos climatológicos
    """)

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 8: IMPUTACIÓN POR MEDIA AGRUPADA POR ESTACIÓN METEOROLÓGICA")
    print("=" * 80)
    
    # Crear datos
    df_original = crear_datos_temperaturas()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Analizar datos meteorológicos
    analizar_datos_meteorologicos(df_original)
    
    # Validar consistencia temporal
    validar_consistencia_temporal(df_original)
    
    # Analizar patrones estacionales
    analizar_patrones_estacionales(df_original)
    
    # Validar calidad de datos
    validar_calidad_datos_meteorologicos(df_original)
    
    # Realizar imputación
    df_imputado, _ = imputar_por_media_estacion(df_original)
    
    # Mostrar resultados
    mostrar_resultados_imputacion(df_original, df_imputado)
    
    # Comparar estaciones climáticas
    comparar_estaciones_climaticas(df_imputado)
    
    # Explicar ventajas de la media
    explicar_ventajas_media_meteorologica()
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Temperatura'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
