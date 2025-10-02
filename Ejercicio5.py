"""
Ejercicio 5 - Mediana por curso
Imputación de datos faltantes en calificaciones de proyecto final
por curso utilizando la mediana por curso para reducir influencia de valores atípicos.
"""

import pandas as pd
import numpy as np

def crear_datos_calificaciones():
    """
    Crea los datos de calificaciones con valores faltantes según el enunciado
    """
    # Datos del Curso A (20 estudiantes)
    curso_a = [3.0, 3.5, 4.0, np.nan, 3.8, 3.2, 3.5, 3.0, np.nan, 3.6, 
               3.7, np.nan, 3.4, 3.5, 3.8, 3.0, 3.6, np.nan, 3.2, 3.5]
    
    # Datos del Curso B (20 estudiantes)
    curso_b = [4.5, 4.7, 4.8, np.nan, 4.9, 4.6, 4.8, 4.7, np.nan, 4.9, 
               4.5, 4.8, np.nan, 4.7, 4.9, 4.6, 4.8, 4.7, np.nan, 4.9]
    
    # Datos del Curso C (20 estudiantes)
    curso_c = [2.8, 3.0, 3.2, np.nan, 2.9, 3.1, 3.0, 2.8, np.nan, 3.2, 
               3.1, np.nan, 2.9, 3.0, 3.1, 2.8, 3.2, np.nan, 2.9, 3.0]
    
    # Crear DataFrame
    datos = {
        'Curso': ['Curso A'] * 20 + ['Curso B'] * 20 + ['Curso C'] * 20,
        'Calificacion': curso_a + curso_b + curso_c
    }
    
    df = pd.DataFrame(datos)
    return df

def imputar_por_mediana_curso(df):
    """
    Imputa los valores faltantes utilizando la mediana de calificaciones por curso
    """
    df_imputado = df.copy()
    
    # Calcular la mediana por curso (ignorando valores NaN)
    medianas_curso = df.groupby('Curso')['Calificacion'].median()
    
    print("=== MEDIANAS DE CALIFICACIONES POR CURSO ===")
    for curso, mediana in medianas_curso.items():
        print(f"{curso}: {mediana:.2f} puntos")
    
    # Imputar valores faltantes con la mediana de cada curso
    for curso in df['Curso'].unique():
        mascara_curso = df['Curso'] == curso
        mascara_nan = df['Calificacion'].isna()
        mascara_imputar = mascara_curso & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Calificacion'] = medianas_curso[curso]
    
    return df_imputado, medianas_curso

def analizar_valores_atipicos(df):
    """
    Analiza la presencia de valores atípicos y justifica el uso de la mediana
    """
    print("\n=== ANÁLISIS DE VALORES ATÍPICOS ===")
    
    for curso in df['Curso'].unique():
        datos_curso = df[df['Curso'] == curso]['Calificacion'].dropna()
        
        # Calcular estadísticas
        media = datos_curso.mean()
        mediana = datos_curso.median()
        desv_std = datos_curso.std()
        
        # Cuartiles y rango intercuartílico
        q1 = datos_curso.quantile(0.25)
        q3 = datos_curso.quantile(0.75)
        iqr = q3 - q1
        
        # Límites para detectar valores atípicos (método IQR)
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        # Identificar valores atípicos
        outliers = datos_curso[(datos_curso < limite_inferior) | (datos_curso > limite_superior)]
        
        # Límites más estrictos (método 2*IQR)
        limite_inf_estricto = q1 - 2 * iqr
        limite_sup_estricto = q3 + 2 * iqr
        outliers_extremos = datos_curso[(datos_curso < limite_inf_estricto) | (datos_curso > limite_sup_estricto)]
        
        print(f"\n{curso}:")
        print(f"  Media: {media:.3f}")
        print(f"  Mediana: {mediana:.2f}")
        print(f"  Diferencia Media-Mediana: {abs(media - mediana):.3f}")
        print(f"  Desviación estándar: {desv_std:.3f}")
        print(f"  Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
        print(f"  Límites normales (1.5*IQR): [{limite_inferior:.2f}, {limite_superior:.2f}]")
        print(f"  Valores atípicos moderados: {len(outliers)}")
        if len(outliers) > 0:
            print(f"    Valores: {list(outliers.round(2))}")
        print(f"  Valores atípicos extremos: {len(outliers_extremos)}")
        if len(outliers_extremos) > 0:
            print(f"    Valores: {list(outliers_extremos.round(2))}")

def analizar_robustez_mediana_vs_media(df):
    """
    Compara la robustez de la mediana vs la media ante valores atípicos
    """
    print("\n=== ROBUSTEZ: MEDIANA VS MEDIA ===")
    
    for curso in df['Curso'].unique():
        datos_curso = df[df['Curso'] == curso]['Calificacion'].dropna()
        
        media_original = datos_curso.mean()
        mediana_original = datos_curso.median()
        
        # Simular introducción de un valor atípico extremo
        datos_con_outlier = pd.concat([datos_curso, pd.Series([1.0])])  # Agregar calificación muy baja
        
        media_con_outlier = datos_con_outlier.mean()
        mediana_con_outlier = datos_con_outlier.median()
        
        # Calcular cambio porcentual
        cambio_media = abs(media_con_outlier - media_original) / media_original * 100
        cambio_mediana = abs(mediana_con_outlier - mediana_original) / mediana_original * 100
        
        print(f"\n{curso} - Simulación con valor atípico (1.0):")
        print(f"  Media original: {media_original:.3f}")
        print(f"  Media con outlier: {media_con_outlier:.3f}")
        print(f"  Cambio en media: {cambio_media:.2f}%")
        print(f"  Mediana original: {mediana_original:.2f}")
        print(f"  Mediana con outlier: {mediana_con_outlier:.2f}")
        print(f"  Cambio en mediana: {cambio_mediana:.2f}%")
        print(f"  → La mediana es {cambio_media/cambio_mediana:.1f}x más robusta")

def analizar_distribucion_calificaciones(df):
    """
    Analiza la distribución de calificaciones por curso
    """
    print("\n=== DISTRIBUCIÓN DE CALIFICACIONES POR CURSO ===")
    
    for curso in df['Curso'].unique():
        datos_curso = df[df['Curso'] == curso]['Calificacion'].dropna()
        
        # Crear rangos de calificaciones
        rangos = {
            'Excelente (4.5-5.0)': len(datos_curso[datos_curso >= 4.5]),
            'Sobresaliente (4.0-4.4)': len(datos_curso[(datos_curso >= 4.0) & (datos_curso < 4.5)]),
            'Aceptable (3.5-3.9)': len(datos_curso[(datos_curso >= 3.5) & (datos_curso < 4.0)]),
            'Insuficiente (3.0-3.4)': len(datos_curso[(datos_curso >= 3.0) & (datos_curso < 3.5)]),
            'Deficiente (<3.0)': len(datos_curso[datos_curso < 3.0])
        }
        
        total_estudiantes = len(datos_curso)
        
        print(f"\n{curso} (Total: {total_estudiantes} estudiantes):")
        for rango, cantidad in rangos.items():
            porcentaje = (cantidad / total_estudiantes) * 100 if total_estudiantes > 0 else 0
            print(f"  {rango}: {cantidad} estudiantes ({porcentaje:.1f}%)")
        
        # Estadísticas adicionales
        print(f"  Promedio del curso: {datos_curso.mean():.3f}")
        print(f"  Mediana del curso: {datos_curso.median():.2f}")
        print(f"  Calificación mínima: {datos_curso.min():.1f}")
        print(f"  Calificación máxima: {datos_curso.max():.1f}")

def mostrar_resultados(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for curso in df_original['Curso'].unique():
        datos_curso = df_original[df_original['Curso'] == curso]
        valores_faltantes = datos_curso['Calificacion'].isna().sum()
        total_registros = len(datos_curso)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\n{curso}:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for curso in df_original['Curso'].unique():
        print(f"\n{curso}:")
        
        # Datos originales
        datos_orig = df_original[df_original['Curso'] == curso]['Calificacion']
        datos_imput = df_imputado[df_imputado['Curso'] == curso]['Calificacion']
        
        print("  Datos originales:")
        valores_orig = [f"{x:.1f}" if not pd.isna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f"{x:.2f}" for x in datos_imput]
        print(f"    {valores_imput}")
    
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS COMPARATIVAS ===")
    
    for curso in df_original['Curso'].unique():
        datos_orig = df_original[df_original['Curso'] == curso]['Calificacion']
        datos_imput = df_imputado[df_imputado['Curso'] == curso]['Calificacion']
        
        print(f"\n{curso}:")
        print(f"  Media original (sin NaN): {datos_orig.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Mediana original: {datos_orig.median():.2f}")
        print(f"  Mediana después de imputación: {datos_imput.median():.2f}")
        print(f"  Desviación estándar original: {datos_orig.std():.3f}")
        print(f"  Desviación estándar imputada: {datos_imput.std():.3f}")

def explicar_ventajas_mediana_calificaciones():
    """
    Explica las ventajas específicas de usar mediana para calificaciones
    """
    print("\n" + "="*80)
    print("VENTAJAS DE LA MEDIANA PARA CALIFICACIONES ACADÉMICAS")
    print("="*80)
    print("""
1. ROBUSTEZ ANTE VALORES ATÍPICOS:
   - Las calificaciones pueden tener valores extremos (muy altas o muy bajas)
   - La mediana no se ve afectada por estos valores atípicos
   - Representa mejor el desempeño "típico" del curso
   
2. REPRESENTATIVIDAD DEL CENTRO:
   - 50% de estudiantes están por encima de la mediana
   - 50% de estudiantes están por debajo de la mediana
   - Punto de referencia natural para evaluar desempeño
   
3. ESTABILIDAD EN EVALUACIONES:
   - Menos sensible a errores de calificación extremos
   - No se distorsiona por estudiantes excepcionales (muy altos o muy bajos)
   - Mantiene el nivel característico del curso
   
4. INTERPRETACIÓN PEDAGÓGICA:
   - Fácil de comunicar a estudiantes y padres
   - Representa el nivel de desempeño central del grupo
   - Útil para comparaciones entre cursos
   
5. APROPIADA PARA ESCALAS ORDINALES:
   - Las calificaciones tienen naturaleza ordinal
   - La mediana respeta este orden natural
   - No asume distribución normal de las calificaciones
   
6. RESISTENCIA A SESGOS:
   - Menos influenciada por criterios de calificación inconsistentes
   - Robusta ante pequeños errores en la evaluación
   - Mantiene la integridad de la distribución original

CASOS ESPECÍFICOS EN EDUCACIÓN:
- Cursos con rendimiento muy heterogéneo
- Presencia de estudiantes con necesidades especiales
- Evaluaciones con criterios subjetivos
- Comparación entre diferentes métodos de enseñanza
    """)

def comparar_cursos_tras_imputacion(df_imputado):
    """
    Compara el rendimiento entre cursos después de la imputación
    """
    print("\n=== COMPARACIÓN ENTRE CURSOS (POST-IMPUTACIÓN) ===")
    
    # Estadísticas por curso
    resumen = df_imputado.groupby('Curso')['Calificacion'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(3)
    
    print("\nResumen estadístico:")
    print(resumen)
    
    # Ranking de cursos
    medias_curso = df_imputado.groupby('Curso')['Calificacion'].mean().sort_values(ascending=False)
    medianas_curso = df_imputado.groupby('Curso')['Calificacion'].median().sort_values(ascending=False)
    
    print("\nRanking por promedio:")
    for i, (curso, media) in enumerate(medias_curso.items(), 1):
        print(f"  {i}. {curso}: {media:.3f} puntos")
    
    print("\nRanking por mediana:")
    for i, (curso, mediana) in enumerate(medianas_curso.items(), 1):
        print(f"  {i}. {curso}: {mediana:.2f} puntos")
    
    # Análisis de dispersión
    print("\nAnálisis de consistencia (menor desviación = más consistente):")
    desviaciones = df_imputado.groupby('Curso')['Calificacion'].std().sort_values()
    for curso, desv in desviaciones.items():
        print(f"  {curso}: σ = {desv:.3f} (CV = {(desv/medias_curso[curso]*100):.1f}%)")

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 5: IMPUTACIÓN POR MEDIANA AGRUPADA POR CURSO")
    print("=" * 75)
    
    # Crear datos
    df_original = crear_datos_calificaciones()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Analizar distribución de calificaciones
    analizar_distribucion_calificaciones(df_original)
    
    # Analizar valores atípicos
    analizar_valores_atipicos(df_original)
    
    # Analizar robustez de mediana vs media
    analizar_robustez_mediana_vs_media(df_original)
    
    # Realizar imputación
    df_imputado, _ = imputar_por_mediana_curso(df_original)
    
    # Mostrar resultados detallados
    mostrar_resultados(df_original, df_imputado)
    
    # Comparar cursos tras imputación
    comparar_cursos_tras_imputacion(df_imputado)
    
    # Explicar ventajas de la mediana
    explicar_ventajas_mediana_calificaciones()
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Calificacion'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
