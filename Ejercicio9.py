"""
EJERCICIO 9: IMPUTACIÓN POR MEDIA AGRUPADA POR SEXO Y RANGO ETARIO
================================================================

Estudio nutricional con datos de peso corporal (kg) de diferentes grupos poblacionales.
Se implementa imputación por media estratificada por sexo y rango etario para preservar
los perfiles antropométricos característicos de cada subgrupo demográfico.

Autor: Sistema de Análisis de Datos Nutricionales
Fecha: Octubre 2025
"""

import pandas as pd
import numpy as np

def crear_datos_nutricionales():
    """
    Crea el dataset de estudio nutricional con datos de peso corporal
    organizados por sexo y rango etario, incluyendo valores faltantes.
    
    Returns:
        pd.DataFrame: Dataset con columnas Sexo, Rango_Etario, ID_Participante, Peso
    """
    
    # Datos de mujeres jóvenes (peso en kg)
    pesos_mujeres_jovenes = [55, np.nan, 60, 58, 56, 57, np.nan, 59, 61, 62, 
                            54, 55, np.nan, 60, 58, 57, 59, np.nan, 61, 56]
    
    # Datos de hombres jóvenes (peso en kg)
    pesos_hombres_jovenes = [70, 75, np.nan, 72, 71, 74, 76, np.nan, 73, 72, 
                            70, 71, np.nan, 74, 76, 75, 73, np.nan, 72, 70]
    
    # Datos de adultos mayores (sin distinción de sexo en los datos originales)
    pesos_adultos_mayores = [68, 72, 70, 71, np.nan, 73, 69, 72, 70, 71, 
                            np.nan, 68, 70, 72, 69, 71, np.nan, 70, 72, 71]
    
    # Crear DataFrame estructurado
    datos = []
    
    # Mujeres jóvenes
    for i, peso in enumerate(pesos_mujeres_jovenes, 1):
        datos.append({
            'ID_Participante': f'MJ_{i:03d}',
            'Sexo': 'Mujer',
            'Rango_Etario': 'Joven (18-35 años)',
            'Peso_kg': peso,
            'Grupo': 'Mujer_Joven'
        })
    
    # Hombres jóvenes
    for i, peso in enumerate(pesos_hombres_jovenes, 1):
        datos.append({
            'ID_Participante': f'HJ_{i:03d}',
            'Sexo': 'Hombre',
            'Rango_Etario': 'Joven (18-35 años)',
            'Peso_kg': peso,
            'Grupo': 'Hombre_Joven'
        })
    
    # Adultos mayores (distribuidos equitativamente entre sexos)
    for i, peso in enumerate(pesos_adultos_mayores, 1):
        sexo = 'Mujer' if i % 2 == 1 else 'Hombre'
        prefijo = 'MA' if sexo == 'Mujer' else 'HA'
        datos.append({
            'ID_Participante': f'{prefijo}_{i:03d}',
            'Sexo': sexo,
            'Rango_Etario': 'Adulto Mayor (>60 años)',
            'Peso_kg': peso,
            'Grupo': f'{sexo}_Adulto_Mayor'
        })
    
    return pd.DataFrame(datos)

def calcular_parametros_nutricionales(datos):
    """
    Calcula parámetros nutricionales y antropométricos por grupo demográfico.
    
    Args:
        datos (pd.DataFrame): Dataset de estudio nutricional
        
    Returns:
        dict: Estadísticas nutricionales por grupo
    """
    
    estadisticas = {}
    
    for grupo in datos['Grupo'].unique():
        datos_grupo = datos[datos['Grupo'] == grupo]['Peso_kg'].dropna()
        
        if len(datos_grupo) > 0:
            # Estadísticas básicas
            media = datos_grupo.mean()
            mediana = datos_grupo.median()
            std = datos_grupo.std()
            cv = (std / media) * 100
            
            # Percentiles antropométricos
            p10 = datos_grupo.quantile(0.10)
            p25 = datos_grupo.quantile(0.25)
            p75 = datos_grupo.quantile(0.75)
            p90 = datos_grupo.quantile(0.90)
            
            # Clasificación nutricional (basada en rangos típicos)
            clasificacion = clasificar_estado_nutricional(media, grupo)
            
            # Variabilidad antropométrica
            rango = datos_grupo.max() - datos_grupo.min()
            
            estadisticas[grupo] = {
                'n_validos': len(datos_grupo),
                'media': round(media, 2),
                'mediana': round(mediana, 2),
                'std': round(std, 2),
                'cv': round(cv, 2),
                'min': round(datos_grupo.min(), 1),
                'max': round(datos_grupo.max(), 1),
                'rango': round(rango, 1),
                'p10': round(p10, 1),
                'p25': round(p25, 1),
                'p75': round(p75, 1),
                'p90': round(p90, 1),
                'clasificacion': clasificacion
            }
    
    return estadisticas

def clasificar_estado_nutricional(peso_promedio, grupo):
    """
    Clasifica el estado nutricional basado en el peso promedio y características del grupo.
    
    Args:
        peso_promedio (float): Peso promedio del grupo
        grupo (str): Identificador del grupo demográfico
        
    Returns:
        str: Clasificación nutricional
    """
    
    if 'Mujer_Joven' in grupo:
        if peso_promedio < 50:
            return 'Bajo peso'
        elif peso_promedio < 65:
            return 'Peso normal'
        elif peso_promedio < 75:
            return 'Sobrepeso'
        else:
            return 'Obesidad'
    
    elif 'Hombre_Joven' in grupo:
        if peso_promedio < 60:
            return 'Bajo peso'
        elif peso_promedio < 80:
            return 'Peso normal'
        elif peso_promedio < 95:
            return 'Sobrepeso'
        else:
            return 'Obesidad'
    
    else:  # Adultos mayores
        if peso_promedio < 55:
            return 'Bajo peso'
        elif peso_promedio < 75:
            return 'Peso normal'
        elif peso_promedio < 85:
            return 'Sobrepeso'
        else:
            return 'Obesidad'

def analizar_distribucion_poblacional(datos):
    """
    Analiza la distribución de pesos por características demográficas.
    
    Args:
        datos (pd.DataFrame): Dataset de estudio nutricional
        
    Returns:
        dict: Análisis demográfico detallado
    """
    
    analisis = {}
    
    # Análisis por sexo
    print("\n=== ANÁLISIS DEMOGRÁFICO POR SEXO ===")
    for sexo in datos['Sexo'].unique():
        datos_sexo = datos[datos['Sexo'] == sexo]['Peso_kg'].dropna()
        media_sexo = datos_sexo.mean()
        std_sexo = datos_sexo.std()
        n_sexo = len(datos_sexo)
        
        print(f"\n{sexo}:")
        print(f"  N participantes: {n_sexo}")
        print(f"  Peso promedio: {media_sexo:.2f} kg")
        print(f"  Desviación estándar: {std_sexo:.2f} kg")
        print(f"  Rango: {datos_sexo.min():.1f} - {datos_sexo.max():.1f} kg")
        print(f"  Coeficiente de variación: {(std_sexo/media_sexo)*100:.2f}%")
        
        analisis[sexo] = {
            'n': n_sexo,
            'media': round(media_sexo, 2),
            'std': round(std_sexo, 2),
            'min': round(datos_sexo.min(), 1),
            'max': round(datos_sexo.max(), 1)
        }
    
    # Análisis por rango etario
    print("\n=== ANÁLISIS DEMOGRÁFICO POR RANGO ETARIO ===")
    for rango in datos['Rango_Etario'].unique():
        datos_rango = datos[datos['Rango_Etario'] == rango]['Peso_kg'].dropna()
        media_rango = datos_rango.mean()
        std_rango = datos_rango.std()
        n_rango = len(datos_rango)
        
        print(f"\n{rango}:")
        print(f"  N participantes: {n_rango}")
        print(f"  Peso promedio: {media_rango:.2f} kg")
        print(f"  Desviación estándar: {std_rango:.2f} kg")
        print(f"  Rango: {datos_rango.min():.1f} - {datos_rango.max():.1f} kg")
        print(f"  Coeficiente de variación: {(std_rango/media_rango)*100:.2f}%")
        
        analisis[rango] = {
            'n': n_rango,
            'media': round(media_rango, 2),
            'std': round(std_rango, 2),
            'min': round(datos_rango.min(), 1),
            'max': round(datos_rango.max(), 1)
        }
    
    return analisis

def validar_coherencia_antropometrica(datos_originales, datos_imputados):
    """
    Valida la coherencia antropométrica después de la imputación.
    
    Args:
        datos_originales (pd.DataFrame): Datos antes de imputación
        datos_imputados (pd.DataFrame): Datos después de imputación
        
    Returns:
        dict: Resultados de validación antropométrica
    """
    
    validacion = {}
    
    print("\n=== VALIDACIÓN DE COHERENCIA ANTROPOMÉTRICA ===")
    
    for grupo in datos_originales['Grupo'].unique():
        # Datos originales (sin NaN)
        orig_grupo = datos_originales[datos_originales['Grupo'] == grupo]['Peso_kg'].dropna()
        
        # Datos imputados (completos)
        imput_grupo = datos_imputados[datos_imputados['Grupo'] == grupo]['Peso_kg']
        
        # Calcular diferencias
        diff_media = abs(orig_grupo.mean() - imput_grupo.mean())
        diff_std = abs(orig_grupo.std() - imput_grupo.std())
        diff_mediana = abs(orig_grupo.median() - imput_grupo.median())
        
        # Porcentaje de datos imputados
        n_total = len(datos_originales[datos_originales['Grupo'] == grupo])
        n_faltantes = n_total - len(orig_grupo)
        pct_imputados = (n_faltantes / n_total) * 100
        
        # Validación de rangos fisiológicos
        valores_imputados = datos_imputados[
            (datos_imputados['Grupo'] == grupo) & 
            (datos_originales[datos_originales['Grupo'] == grupo]['Peso_kg'].isna())
        ]['Peso_kg']
        
        # Verificar si los valores imputados están dentro del rango esperado
        rango_min = orig_grupo.min() - 2 * orig_grupo.std()
        rango_max = orig_grupo.max() + 2 * orig_grupo.std()
        valores_atipicos = sum((valores_imputados < rango_min) | (valores_imputados > rango_max))
        
        print(f"\n{grupo}:")
        print(f"  Datos imputados: {n_faltantes}/{n_total} ({pct_imputados:.1f}%)")
        print(f"  Diferencia en media: {diff_media:.3f} kg")
        print(f"  Diferencia en mediana: {diff_mediana:.3f} kg")
        print(f"  Diferencia en std: {diff_std:.3f} kg")
        print(f"  Valores atípicos imputados: {valores_atipicos}")
        print(f"  Coherencia antropométrica: {'✓ Excelente' if diff_media < 0.5 else '⚠ Aceptable' if diff_media < 1.0 else '✗ Revisar'}")
        
        validacion[grupo] = {
            'n_imputados': n_faltantes,
            'pct_imputados': round(pct_imputados, 1),
            'diff_media': round(diff_media, 3),
            'diff_mediana': round(diff_mediana, 3),
            'diff_std': round(diff_std, 3),
            'valores_atipicos': valores_atipicos,
            'coherencia': 'Excelente' if diff_media < 0.5 else 'Aceptable' if diff_media < 1.0 else 'Revisar'
        }
    
    return validacion

def imputar_por_media_grupo_demografico(datos):
    """
    Imputa valores faltantes usando la media por grupo demográfico (sexo × rango etario).
    
    Args:
        datos (pd.DataFrame): Dataset con valores faltantes
        
    Returns:
        tuple: (datos_imputados, medias_por_grupo, resumen_imputacion)
    """
    
    datos_imputados = datos.copy()
    medias_por_grupo = {}
    resumen_imputacion = {}
    
    print("\n=== CÁLCULO DE MEDIAS POR GRUPO DEMOGRÁFICO ===")
    
    # Calcular medias por grupo
    for grupo in datos['Grupo'].unique():
        datos_grupo = datos[datos['Grupo'] == grupo]['Peso_kg']
        media_grupo = datos_grupo.mean()  # Automáticamente excluye NaN
        medias_por_grupo[grupo] = media_grupo
        
        # Contar valores faltantes
        n_faltantes = datos_grupo.isna().sum()
        n_total = len(datos_grupo)
        
        print(f"{grupo}: {media_grupo:.3f} kg (imputará {n_faltantes}/{n_total} valores)")
        
        resumen_imputacion[grupo] = {
            'media': round(media_grupo, 3),
            'n_faltantes': n_faltantes,
            'n_total': n_total,
            'pct_faltantes': round((n_faltantes/n_total)*100, 1)
        }
    
    # Realizar imputación
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    
    for grupo in datos['Grupo'].unique():
        mask_grupo = datos_imputados['Grupo'] == grupo
        mask_faltantes = datos_imputados['Peso_kg'].isna()
        mask_imputar = mask_grupo & mask_faltantes
        
        if mask_imputar.any():
            datos_imputados.loc[mask_imputar, 'Peso_kg'] = medias_por_grupo[grupo]
            n_imputados = mask_imputar.sum()
            print(f"✓ {grupo}: {n_imputados} valores imputados con {medias_por_grupo[grupo]:.3f} kg")
    
    return datos_imputados, medias_por_grupo, resumen_imputacion

def analizar_diferencias_demograficas(datos):
    """
    Analiza las diferencias significativas entre grupos demográficos.
    
    Args:
        datos (pd.DataFrame): Dataset completo después de imputación
        
    Returns:
        dict: Análisis de diferencias entre grupos
    """
    
    print("\n=== ANÁLISIS DE DIFERENCIAS DEMOGRÁFICAS ===")
    
    grupos = datos['Grupo'].unique()
    diferencias = {}
    
    # Comparaciones por pares entre grupos
    for i, grupo1 in enumerate(grupos):
        for grupo2 in grupos[i+1:]:
            peso1 = datos[datos['Grupo'] == grupo1]['Peso_kg']
            peso2 = datos[datos['Grupo'] == grupo2]['Peso_kg']
            
            diff_media = peso1.mean() - peso2.mean()
            diff_std = peso1.std() - peso2.std()
            
            # Calcular overlap de distribuciones (aproximado)
            min1, max1 = peso1.min(), peso1.max()
            min2, max2 = peso2.min(), peso2.max()
            overlap = max(0, min(max1, max2) - max(min1, min2))
            total_range = max(max1, max2) - min(min1, min2)
            pct_overlap = (overlap / total_range) * 100 if total_range > 0 else 0
            
            print(f"\n{grupo1} vs {grupo2}:")
            print(f"  Diferencia en peso promedio: {diff_media:+.2f} kg")
            print(f"  Diferencia en variabilidad: {diff_std:+.2f} kg")
            print(f"  Overlap de rangos: {pct_overlap:.1f}%")
            
            if abs(diff_media) > 5:
                significancia = "Muy significativa"
            elif abs(diff_media) > 2:
                significancia = "Significativa"
            else:
                significancia = "Leve"
                
            print(f"  Significancia clínica: {significancia}")
            
            diferencias[f"{grupo1}_vs_{grupo2}"] = {
                'diff_media': round(diff_media, 2),
                'diff_std': round(diff_std, 2),
                'overlap_pct': round(pct_overlap, 1),
                'significancia': significancia
            }
    
    return diferencias

def main():
    """
    Función principal que ejecuta el análisis completo del estudio nutricional.
    """
    
    print("EJERCICIO 9: IMPUTACIÓN POR MEDIA AGRUPADA POR SEXO Y RANGO ETARIO")
    print("=" * 80)
    
    # 1. Crear datos
    datos_originales = crear_datos_nutricionales()
    
    print("\nDATOS ORIGINALES DEL ESTUDIO NUTRICIONAL:")
    print(datos_originales.head(15))
    print(f"\nDimensiones: {datos_originales.shape}")
    print(f"Valores faltantes totales: {datos_originales['Peso_kg'].isna().sum()}")
    
    # 2. Análisis nutricional inicial
    estadisticas_nutricionales = calcular_parametros_nutricionales(datos_originales)
    
    print("\n=== PARÁMETROS NUTRICIONALES POR GRUPO DEMOGRÁFICO ===")
    for grupo, stats in estadisticas_nutricionales.items():
        print(f"\n{grupo}:")
        print(f"  N válidos: {stats['n_validos']}")
        print(f"  Peso promedio: {stats['media']} kg")
        print(f"  Mediana: {stats['mediana']} kg")
        print(f"  Desviación estándar: {stats['std']} kg")
        print(f"  Coeficiente de variación: {stats['cv']}%")
        print(f"  Rango: {stats['min']} - {stats['max']} kg")
        print(f"  Percentiles (P10-P90): {stats['p10']} - {stats['p90']} kg")
        print(f"  Clasificación nutricional: {stats['clasificacion']}")
    
    # 3. Análisis demográfico
    analisis_demografico = analizar_distribucion_poblacional(datos_originales)
    
    # 4. Análisis de datos faltantes
    print("\n=== ANÁLISIS DE DATOS FALTANTES POR GRUPO ===")
    for grupo in datos_originales['Grupo'].unique():
        datos_grupo = datos_originales[datos_originales['Grupo'] == grupo]
        n_total = len(datos_grupo)
        n_faltantes = datos_grupo['Peso_kg'].isna().sum()
        pct_faltantes = (n_faltantes / n_total) * 100
        
        print(f"{grupo}:")
        print(f"  Total participantes: {n_total}")
        print(f"  Datos faltantes: {n_faltantes} ({pct_faltantes:.1f}%)")
        print(f"  Datos válidos: {n_total - n_faltantes}")
    
    # 5. Imputación por media de grupo demográfico
    datos_imputados, medias_grupos, resumen = imputar_por_media_grupo_demografico(datos_originales)
    
    # 6. Comparación antes/después
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS DE IMPUTACIÓN ===")
    
    for grupo in datos_originales['Grupo'].unique():
        datos_orig = datos_originales[datos_originales['Grupo'] == grupo]['Peso_kg']
        datos_imput = datos_imputados[datos_imputados['Grupo'] == grupo]['Peso_kg']
        
        print(f"\n{grupo}:")
        print(f"  Datos originales (primeros 10):")
        print(f"    {[f'{x:.1f}' if not pd.isna(x) else 'NaN' for x in datos_orig.head(10).values]}")
        print(f"  Datos imputados (primeros 10):")
        print(f"    {[f'{x:.3f}' for x in datos_imput.head(10).values]}")
        
        # Estadísticas comparativas
        orig_sin_nan = datos_orig.dropna()
        print(f"  Media original (sin NaN): {orig_sin_nan.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Mediana original: {orig_sin_nan.median():.3f}")
        print(f"  Mediana después de imputación: {datos_imput.median():.3f}")
        print(f"  Std original: {orig_sin_nan.std():.3f}")
        print(f"  Std después de imputación: {datos_imput.std():.3f}")
    
    # 7. Validación antropométrica
    validacion = validar_coherencia_antropometrica(datos_originales, datos_imputados)
    
    # 8. Análisis de diferencias demográficas
    diferencias = analizar_diferencias_demograficas(datos_imputados)
    
    # 9. Resumen estadístico final
    print("\n=== RESUMEN ESTADÍSTICO COMPARATIVO FINAL ===")
    resumen_final = datos_imputados.groupby('Grupo')['Peso_kg'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(2)
    
    print(resumen_final)
    
    # 10. Ranking nutricional
    print("\n=== RANKING NUTRICIONAL POR PESO PROMEDIO ===")
    ranking = datos_imputados.groupby('Grupo')['Peso_kg'].mean().sort_values(ascending=False)
    
    for i, (grupo, peso) in enumerate(ranking.items(), 1):
        print(f"  {i}. {grupo}: {peso:.2f} kg")
    
    # 11. Análisis de variabilidad nutricional
    print("\n=== ANÁLISIS DE VARIABILIDAD NUTRICIONAL ===")
    cv_por_grupo = (datos_imputados.groupby('Grupo')['Peso_kg'].std() / 
                    datos_imputados.groupby('Grupo')['Peso_kg'].mean() * 100).sort_values()
    
    print("Grupos ordenados por estabilidad de peso (menor CV = más estable):")
    for grupo, cv in cv_por_grupo.items():
        estabilidad = "Muy estable" if cv < 5 else "Estable" if cv < 10 else "Variable"
        print(f"  {grupo}: CV = {cv:.2f}% ({estabilidad})")
    
    # 12. Ventajas de la media por grupo demográfico
    print("\n" + "=" * 80)
    print("VENTAJAS DE LA MEDIA POR GRUPO DEMOGRÁFICO (SEXO × RANGO ETARIO)")
    print("=" * 80)
    
    ventajas = [
        "1. PRESERVACIÓN DE PERFILES ANTROPOMÉTRICOS:",
        "   - Mantiene las diferencias de peso entre sexos",
        "   - Conserva las variaciones por edad",
        "   - Respeta las características poblacionales",
        "",
        "2. VALIDEZ EPIDEMIOLÓGICA:",
        "   - Basada en patrones demográficos conocidos",
        "   - Coherente con estudios antropométricos",
        "   - Preserva gradientes nutricionales naturales",
        "",
        "3. PRECISIÓN NUTRICIONAL:",
        "   - Reduce sesgo en análisis por subgrupos",
        "   - Mantiene representatividad poblacional",
        "   - Válida para comparaciones entre grupos",
        "",
        "4. APLICABILIDAD CLÍNICA:",
        "   - Útil para evaluaciones nutricionales",
        "   - Base para recomendaciones dietéticas",
        "   - Coherente con protocolos médicos",
        "",
        "5. ROBUSTEZ ESTADÍSTICA:",
        "   - Minimiza distorsión de medias grupales",
        "   - Preserva variabilidad inter-grupal",
        "   - Mantiene poder estadístico para análisis",
        "",
        "6. INTERPRETACIÓN DEMOGRÁFICA:",
        "   - Refleja realidades poblacionales",
        "   - Facilita análisis epidemiológicos",
        "   - Base para políticas de salud pública",
        "",
        "APLICACIONES ESPECÍFICAS:",
        "- Estudios nutricionales poblacionales",
        "- Evaluaciones antropométricas clínicas",
        "- Investigación en salud pública",
        "- Análisis de seguridad alimentaria",
        "- Diseño de programas nutricionales"
    ]
    
    for ventaja in ventajas:
        print(ventaja)
    
    # 13. Datos finales
    print(f"\n=== DATOS FINALES IMPUTADOS ===")
    print(datos_imputados)
    print(f"\nValores faltantes después de imputación: {datos_imputados['Peso_kg'].isna().sum()}")
    
    return datos_imputados, estadisticas_nutricionales, validacion

if __name__ == "__main__":
    datos_final, stats, validacion = main()
