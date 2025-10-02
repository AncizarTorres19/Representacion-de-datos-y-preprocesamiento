"""
Ejercicio 4 - Media por grupo etario
Imputación de datos faltantes en pasos diarios promedio
por grupos de edad utilizando la media por grupo etario.
"""

import pandas as pd
import numpy as np

def crear_datos_pasos():
    """
    Crea los datos de pasos diarios con valores faltantes según el enunciado
    """
    # Datos de 18-30 años (20 registros)
    grupo_18_30 = [7000, 7500, np.nan, 7200, 7600, 7400, 7300, 7500, np.nan, 7600, 
                   7200, 7400, 7300, 7500, np.nan, 7200, 7600, 7400, 7300, 7500]
    
    # Datos de 31-50 años (20 registros)
    grupo_31_50 = [6000, 6500, np.nan, 6300, 6100, 6400, 6200, 6500, 6300, np.nan, 
                   6400, 6200, 6500, 6300, np.nan, 6100, 6400, 6200, 6500, 6300]
    
    # Datos de 51-70 años (20 registros)
    grupo_51_70 = [4000, 4200, 4100, 3900, 4300, 4100, np.nan, 4200, 4000, 4300, 
                   4100, np.nan, 4200, 4000, 4300, 4100, np.nan, 4200, 4000, 4300]
    
    # Crear DataFrame
    datos = {
        'Grupo_Edad': ['18-30'] * 20 + ['31-50'] * 20 + ['51-70'] * 20,
        'Pasos_Diarios': grupo_18_30 + grupo_31_50 + grupo_51_70
    }
    
    df = pd.DataFrame(datos)
    return df

def imputar_por_media_grupo(df):
    """
    Imputa los valores faltantes utilizando la media de pasos diarios por grupo de edad
    """
    df_imputado = df.copy()
    
    # Calcular la media por grupo de edad (ignorando valores NaN)
    medias_grupo = df.groupby('Grupo_Edad')['Pasos_Diarios'].mean()
    
    print("=== MEDIAS DE PASOS DIARIOS POR GRUPO DE EDAD ===")
    for grupo, media in medias_grupo.items():
        print(f"{grupo} años: {media:.1f} pasos diarios")
    
    # Imputar valores faltantes con la media de cada grupo
    for grupo in df['Grupo_Edad'].unique():
        mascara_grupo = df['Grupo_Edad'] == grupo
        mascara_nan = df['Pasos_Diarios'].isna()
        mascara_imputar = mascara_grupo & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Pasos_Diarios'] = medias_grupo[grupo]
    
    return df_imputado, medias_grupo

def analizar_distribucion_y_asimetria(df):
    """
    Analiza la distribución y asimetría de los datos por grupo
    """
    print("\n=== ANÁLISIS DE DISTRIBUCIÓN Y ASIMETRÍA ===")
    
    for grupo in df['Grupo_Edad'].unique():
        datos_grupo = df[df['Grupo_Edad'] == grupo]['Pasos_Diarios'].dropna()
        
        # Estadísticas descriptivas
        media = datos_grupo.mean()
        mediana = datos_grupo.median()
        desv_std = datos_grupo.std()
        
        # Medidas de asimetría
        asimetria = datos_grupo.skew()
        
        # Cuartiles
        q1 = datos_grupo.quantile(0.25)
        q3 = datos_grupo.quantile(0.75)
        iqr = q3 - q1
        
        # Coeficiente de variación
        cv = (desv_std / media) * 100
        
        print(f"\n{grupo} años:")
        print(f"  Media: {media:.1f} pasos")
        print(f"  Mediana: {mediana:.1f} pasos")
        print(f"  Desviación estándar: {desv_std:.1f} pasos")
        print(f"  Coeficiente de variación: {cv:.2f}%")
        print(f"  Asimetría (skewness): {asimetria:.3f}")
        print(f"  Q1: {q1:.1f}, Q3: {q3:.1f}, IQR: {iqr:.1f}")
        print(f"  Rango: {datos_grupo.min():.0f} - {datos_grupo.max():.0f} pasos")
        
        # Interpretación de la asimetría
        if abs(asimetria) < 0.5:
            interpretacion = "aproximadamente simétrica"
        elif asimetria < -0.5:
            interpretacion = "sesgada hacia la izquierda"
        else:
            interpretacion = "sesgada hacia la derecha"
        
        print(f"  Interpretación: Distribución {interpretacion}")

def validar_uso_media(df):
    """
    Valida por qué la media es apropiada para estos datos
    """
    print("\n=== VALIDACIÓN DEL USO DE LA MEDIA ===")
    
    for grupo in df['Grupo_Edad'].unique():
        datos_grupo = df[df['Grupo_Edad'] == grupo]['Pasos_Diarios'].dropna()
        
        media = datos_grupo.mean()
        mediana = datos_grupo.median()
        diferencia_relativa = abs(media - mediana) / media * 100
        
        # Detectar valores atípicos usando el método IQR
        q1 = datos_grupo.quantile(0.25)
        q3 = datos_grupo.quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        outliers = datos_grupo[(datos_grupo < limite_inferior) | (datos_grupo > limite_superior)]
        
        print(f"\n{grupo} años:")
        print("  Media vs Mediana:")
        print(f"    Media: {media:.1f} pasos")
        print(f"    Mediana: {mediana:.1f} pasos")
        print(f"    Diferencia relativa: {diferencia_relativa:.2f}%")
        
        print(f"  Valores atípicos detectados: {len(outliers)}")
        if len(outliers) > 0:
            print(f"    Valores: {list(outliers.round(0).astype(int))}")
        
        # Evaluación de idoneidad de la media
        if diferencia_relativa < 5 and len(outliers) == 0:
            evaluacion = "✓ MUY APROPIADA"
        elif diferencia_relativa < 10 and len(outliers) <= 1:
            evaluacion = "✓ APROPIADA"
        else:
            evaluacion = "⚠ REVISAR"
        
        print(f"  Evaluación para uso de media: {evaluacion}")

def comparar_con_otros_metodos(df):
    """
    Compara la imputación por media con otros métodos posibles
    """
    print("\n=== COMPARACIÓN CON OTROS MÉTODOS DE IMPUTACIÓN ===")
    
    for grupo in df['Grupo_Edad'].unique():
        datos_grupo = df[df['Grupo_Edad'] == grupo]['Pasos_Diarios'].dropna()
        
        media = datos_grupo.mean()
        mediana = datos_grupo.median()
        
        # Moda (valor más frecuente, aunque para datos continuos es menos relevante)
        moda_valores = datos_grupo.mode()
        moda = moda_valores.iloc[0] if len(moda_valores) > 0 else "N/A"
        
        print(f"\n{grupo} años:")
        print(f"  Media: {media:.1f} pasos")
        print(f"  Mediana: {mediana:.1f} pasos")
        print(f"  Moda: {moda} pasos" if moda != "N/A" else "  Moda: No aplicable (datos continuos)")
        
        # Recomendación
        print("  Recomendación: MEDIA - Ideal para variable continua sin asimetría fuerte")

def mostrar_resultados(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for grupo in df_original['Grupo_Edad'].unique():
        datos_grupo = df_original[df_original['Grupo_Edad'] == grupo]
        valores_faltantes = datos_grupo['Pasos_Diarios'].isna().sum()
        total_registros = len(datos_grupo)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\n{grupo} años:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for grupo in df_original['Grupo_Edad'].unique():
        print(f"\n{grupo} años:")
        
        # Datos originales
        datos_orig = df_original[df_original['Grupo_Edad'] == grupo]['Pasos_Diarios']
        datos_imput = df_imputado[df_imputado['Grupo_Edad'] == grupo]['Pasos_Diarios']
        
        print("  Datos originales:")
        valores_orig = [f"{x:.0f}" if not pd.isna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f"{x:.1f}" for x in datos_imput]
        print(f"    {valores_imput}")
    
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS COMPARATIVAS ===")
    
    for grupo in df_original['Grupo_Edad'].unique():
        datos_orig = df_original[df_original['Grupo_Edad'] == grupo]['Pasos_Diarios']
        datos_imput = df_imputado[df_imputado['Grupo_Edad'] == grupo]['Pasos_Diarios']
        
        print(f"\n{grupo} años:")
        print(f"  Media original (sin NaN): {datos_orig.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Mediana original: {datos_orig.median():.1f}")
        print(f"  Mediana después de imputación: {datos_imput.median():.1f}")
        print(f"  Desviación estándar original: {datos_orig.std():.3f}")
        print(f"  Desviación estándar imputada: {datos_imput.std():.3f}")

def explicar_ventajas_media_continua():
    """
    Explica las ventajas de usar media para variables continuas
    """
    print("\n" + "="*75)
    print("VENTAJAS DE LA MEDIA PARA VARIABLES CONTINUAS SIN ASIMETRÍA")
    print("="*75)
    print("""
1. ADECUADA PARA VARIABLES CONTINUAS:
   - Los pasos diarios son una variable continua cuantitativa
   - La media utiliza toda la información disponible de los datos
   
2. ÓPTIMA PARA DISTRIBUCIONES SIMÉTRICAS:
   - Cuando no hay asimetría fuerte, la media = mediana ≈ moda
   - Representa el verdadero centro de la distribución
   
3. MINIMIZA LA VARIANZA:
   - La media minimiza la suma de cuadrados de las desviaciones
   - Propiedad matemática que la hace estadísticamente óptima
   
4. PRESERVA LA MEDIA ORIGINAL:
   - La media del grupo se mantiene constante tras la imputación
   - No introduce sesgo en la estimación
   
5. INTERPRETACIÓN INTUITIVA:
   - Representa el "valor típico" o "promedio" del grupo
   - Fácil de comunicar y entender
   
6. ESTABILIDAD ESTADÍSTICA:
   - Menos sensible a pequeñas variaciones que otros métodos
   - Converge al valor poblacional con muestras grandes
   
7. COHERENCIA CON EL ANÁLISIS POSTERIOR:
   - Compatible con análisis estadísticos paramétricos
   - Mantiene las propiedades distribucionales originales

CUÁNDO USAR LA MEDIA:
✓ Variable continua
✓ Distribución aproximadamente simétrica  
✓ Pocos o ningún valor atípico extremo
✓ Tamaño de muestra adecuado
    """)

def crear_resumen_por_grupo_edad(df_imputado):
    """
    Crea un resumen final de los datos por grupo de edad
    """
    print("\n=== RESUMEN FINAL POR GRUPO DE EDAD ===")
    
    resumen = df_imputado.groupby('Grupo_Edad')['Pasos_Diarios'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(1)
    
    print(resumen)
    
    print("\n=== INTERPRETACIÓN DE TENDENCIAS ===")
    medias_ordenadas = df_imputado.groupby('Grupo_Edad')['Pasos_Diarios'].mean().sort_values(ascending=False)
    
    print("\nRanking de actividad física por grupo:")
    for i, (grupo, media) in enumerate(medias_ordenadas.items(), 1):
        print(f"  {i}. {grupo} años: {media:.1f} pasos diarios")
    
    # Calcular diferencias entre grupos
    print("\nDiferencias entre grupos consecutivos:")
    grupos_ordenados = ['18-30', '31-50', '51-70']
    for i in range(len(grupos_ordenados) - 1):
        grupo_actual = grupos_ordenados[i]
        grupo_siguiente = grupos_ordenados[i + 1]
        
        media_actual = medias_ordenadas[grupo_actual]
        media_siguiente = medias_ordenadas[grupo_siguiente]
        diferencia = media_actual - media_siguiente
        porcentaje_reduccion = (diferencia / media_actual) * 100
        
        print(f"  {grupo_actual} vs {grupo_siguiente}: -{diferencia:.1f} pasos ({porcentaje_reduccion:.1f}% menos)")

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 4: IMPUTACIÓN POR MEDIA AGRUPADA POR GRUPO ETARIO")
    print("=" * 75)
    
    # Crear datos
    df_original = crear_datos_pasos()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Analizar distribución y asimetría
    analizar_distribucion_y_asimetria(df_original)
    
    # Validar uso de la media
    validar_uso_media(df_original)
    
    # Comparar con otros métodos
    comparar_con_otros_metodos(df_original)
    
    # Realizar imputación
    df_imputado, _ = imputar_por_media_grupo(df_original)
    
    # Mostrar resultados detallados
    mostrar_resultados(df_original, df_imputado)
    
    # Explicar ventajas de la media
    explicar_ventajas_media_continua()
    
    # Crear resumen final
    crear_resumen_por_grupo_edad(df_imputado)
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Pasos_Diarios'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
