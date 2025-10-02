"""
EJERCICIO 10: IMPUTACIÓN POR MEDIA AGRUPADA POR OPERADOR Y TURNO
===============================================================

Call center con datos de duración de llamadas (minutos) por operador y turno.
Se implementa imputación por media estratificada por operador y turno para preservar
los patrones de productividad y carga de trabajo específicos de cada franja horaria.

Autor: Sistema de Análisis de Call Center
Fecha: Octubre 2025
"""

import pandas as pd
import numpy as np

# Constantes para clasificación de productividad
PRODUCTIVIDAD_EXCELENTE = 'Excelente'
PRODUCTIVIDAD_BUENA = 'Buena (eficiente)'
PRODUCTIVIDAD_ACEPTABLE = 'Aceptable (estándar)'
PRODUCTIVIDAD_MEJORABLE = 'Mejorable (lenta)'

# Constantes para análisis de carga
CARGA_ALTA = 'Alta'
CARGA_MEDIA = 'Media'
CARGA_BAJA = 'Baja'

# Constantes para complejidad
COMPLEJIDAD_ALTA = 'Alta'
COMPLEJIDAD_MEDIA = 'Media'
COMPLEJIDAD_BAJA = 'Baja'

def crear_datos_call_center():
    """
    Crea el dataset del call center con datos de duración de llamadas
    organizados por operador y turno, incluyendo valores faltantes.
    
    Returns:
        pd.DataFrame: Dataset con columnas Operador, Turno, ID_Llamada, Duracion_min
    """
    
    # Datos Operador A, turno mañana (duración en minutos)
    # Nota: "vacío" se interpreta como valor faltante
    duraciones_op_a_manana = [5, 6, np.nan, 7, 8, 6, 7, np.nan, 5, 7, 
                              8, 6, 7, np.nan, 6, 8, 7, 5, 6, np.nan]
    
    # Datos Operador B, turno tarde (duración en minutos)
    duraciones_op_b_tarde = [8, 9, np.nan, 7, 8, 10, 9, np.nan, 8, 7, 
                             9, 8, np.nan, 10, 9, 7, 8, 9, 8, 10]
    
    # Datos Operador C, turno noche (duración en minutos)
    duraciones_op_c_noche = [12, 11, 10, 13, np.nan, 12, 11, 10, np.nan, 13, 
                             12, 11, 10, np.nan, 12, 13, 11, 10, 12, 11]
    
    # Crear DataFrame estructurado
    datos = []
    
    # Operador A - Turno Mañana
    for i, duracion in enumerate(duraciones_op_a_manana, 1):
        datos.append({
            'ID_Llamada': f'A_M_{i:03d}',
            'Operador': 'Operador A',
            'Turno': 'Mañana (06:00-14:00)',
            'Franja_Horaria': 'Mañana',
            'Duracion_min': duracion,
            'Grupo_Operativo': 'A_Mañana',
            'Hora_Inicio': f'{6 + (i-1)//3}:{(i-1)%3*20:02d}'
        })
    
    # Operador B - Turno Tarde
    for i, duracion in enumerate(duraciones_op_b_tarde, 1):
        datos.append({
            'ID_Llamada': f'B_T_{i:03d}',
            'Operador': 'Operador B',
            'Turno': 'Tarde (14:00-22:00)',
            'Franja_Horaria': 'Tarde',
            'Duracion_min': duracion,
            'Grupo_Operativo': 'B_Tarde',
            'Hora_Inicio': f'{14 + (i-1)//3}:{(i-1)%3*20:02d}'
        })
    
    # Operador C - Turno Noche
    for i, duracion in enumerate(duraciones_op_c_noche, 1):
        datos.append({
            'ID_Llamada': f'C_N_{i:03d}',
            'Operador': 'Operador C',
            'Turno': 'Noche (22:00-06:00)',
            'Franja_Horaria': 'Noche',
            'Duracion_min': duracion,
            'Grupo_Operativo': 'C_Noche',
            'Hora_Inicio': f'{22 + (i-1)//3 if 22 + (i-1)//3 < 24 else (22 + (i-1)//3) - 24}:{(i-1)%3*20:02d}'
        })
    
    return pd.DataFrame(datos)

def analizar_metricas_call_center(datos):
    """
    Analiza métricas operativas del call center por operador y turno.
    
    Args:
        datos (pd.DataFrame): Dataset del call center
        
    Returns:
        dict: Métricas operativas por grupo
    """
    
    metricas = {}
    
    print("\n=== MÉTRICAS OPERATIVAS POR OPERADOR Y TURNO ===")
    
    for grupo in datos['Grupo_Operativo'].unique():
        datos_grupo = datos[datos['Grupo_Operativo'] == grupo]['Duracion_min'].dropna()
        
        if len(datos_grupo) > 0:
            # Estadísticas de rendimiento
            media = datos_grupo.mean()
            mediana = datos_grupo.median()
            std = datos_grupo.std()
            cv = (std / media) * 100
            
            # Métricas de eficiencia
            min_duracion = datos_grupo.min()
            max_duracion = datos_grupo.max()
            rango = max_duracion - min_duracion
            
            # Percentiles de productividad
            p25 = datos_grupo.quantile(0.25)
            p75 = datos_grupo.quantile(0.75)
            
            # Clasificación de productividad
            clasificacion = clasificar_productividad(media, grupo)
            
            # Índice de consistencia (basado en CV)
            if cv < 10:
                consistencia = "Muy consistente"
            elif cv < 20:
                consistencia = "Consistente"
            elif cv < 30:
                consistencia = "Moderadamente variable"
            else:
                consistencia = "Muy variable"
            
            # Capacidad de llamadas por hora (estimada)
            llamadas_por_hora = 60 / media if media > 0 else 0
            
            print(f"\n{grupo}:")
            print(f"  N llamadas válidas: {len(datos_grupo)}")
            print(f"  Duración promedio: {media:.2f} min")
            print(f"  Mediana: {mediana:.2f} min")
            print(f"  Desviación estándar: {std:.2f} min")
            print(f"  Coeficiente de variación: {cv:.2f}%")
            print(f"  Rango: {min_duracion:.1f} - {max_duracion:.1f} min")
            print(f"  Cuartiles (Q1-Q3): {p25:.1f} - {p75:.1f} min")
            print(f"  Llamadas/hora estimadas: {llamadas_por_hora:.1f}")
            print(f"  Clasificación productividad: {clasificacion}")
            print(f"  Consistencia operativa: {consistencia}")
            
            metricas[grupo] = {
                'n_validas': len(datos_grupo),
                'media': round(media, 2),
                'mediana': round(mediana, 2),
                'std': round(std, 2),
                'cv': round(cv, 2),
                'min': round(min_duracion, 1),
                'max': round(max_duracion, 1),
                'rango': round(rango, 1),
                'q1': round(p25, 1),
                'q3': round(p75, 1),
                'llamadas_hora': round(llamadas_por_hora, 1),
                'clasificacion': clasificacion,
                'consistencia': consistencia
            }
    
    return metricas

def clasificar_productividad(duracion_promedio, grupo):
    """
    Clasifica la productividad basada en la duración promedio de llamadas.
    
    Args:
        duracion_promedio (float): Duración promedio de llamadas
        grupo (str): Identificador del grupo operativo
        
    Returns:
        str: Clasificación de productividad
    """
    
    # Definir umbrales por turno
    if 'Mañana' in grupo:
        umbrales = [6, 7, 8]
        clasificaciones = [
            'Excelente (llamadas rápidas)',
            PRODUCTIVIDAD_BUENA,
            PRODUCTIVIDAD_ACEPTABLE,
            PRODUCTIVIDAD_MEJORABLE
        ]
    elif 'Tarde' in grupo:
        umbrales = [8, 9, 10]
        clasificaciones = [
            'Excelente (muy eficiente)',
            PRODUCTIVIDAD_BUENA,
            PRODUCTIVIDAD_ACEPTABLE,
            PRODUCTIVIDAD_MEJORABLE
        ]
    else:  # Turno noche
        umbrales = [11, 12, 13]
        clasificaciones = [
            'Excelente (muy eficiente)',
            PRODUCTIVIDAD_BUENA,
            PRODUCTIVIDAD_ACEPTABLE,
            PRODUCTIVIDAD_MEJORABLE
        ]
    
    # Determinar clasificación basada en umbrales
    for i, umbral in enumerate(umbrales):
        if duracion_promedio < umbral:
            return clasificaciones[i]
    
    return clasificaciones[-1]

def analizar_patrones_operativos(datos):
    """
    Analiza patrones operativos por franja horaria y operador.
    
    Args:
        datos (pd.DataFrame): Dataset del call center
        
    Returns:
        dict: Análisis de patrones operativos
    """
    
    print("\n=== ANÁLISIS DE PATRONES OPERATIVOS ===")
    
    patrones = {}
    
    # Análisis por operador
    print("\nAnálisis por Operador:")
    for operador in datos['Operador'].unique():
        datos_operador = datos[datos['Operador'] == operador]['Duracion_min'].dropna()
        media_op = datos_operador.mean()
        std_op = datos_operador.std()
        n_op = len(datos_operador)
        
        print(f"\n{operador}:")
        print(f"  Total llamadas: {n_op}")
        print(f"  Duración promedio: {media_op:.2f} min")
        print(f"  Variabilidad: {std_op:.2f} min")
        print(f"  Productividad: {60/media_op:.1f} llamadas/hora")
        
        patrones[operador] = {
            'n_total': n_op,
            'media': round(media_op, 2),
            'std': round(std_op, 2),
            'productividad': round(60/media_op, 1)
        }
    
    # Análisis por turno
    print("\nAnálisis por Turno:")
    for turno in datos['Franja_Horaria'].unique():
        datos_turno = datos[datos['Franja_Horaria'] == turno]['Duracion_min'].dropna()
        media_turno = datos_turno.mean()
        std_turno = datos_turno.std()
        n_turno = len(datos_turno)
        
        print(f"\n{turno}:")
        print(f"  Total llamadas: {n_turno}")
        print(f"  Duración promedio: {media_turno:.2f} min")
        print(f"  Variabilidad: {std_turno:.2f} min")
        # Determinar carga de trabajo
        if media_turno > 10:
            carga_trabajo = CARGA_ALTA
        elif media_turno > 7:
            carga_trabajo = CARGA_MEDIA
        else:
            carga_trabajo = CARGA_BAJA
            
        print(f"  Carga de trabajo: {carga_trabajo}")
        
        patrones[turno] = {
            'n_total': n_turno,
            'media': round(media_turno, 2),
            'std': round(std_turno, 2),
            'carga': carga_trabajo
        }
    
    return patrones

def validar_coherencia_operativa(datos_originales, datos_imputados):
    """
    Valida la coherencia operativa después de la imputación.
    
    Args:
        datos_originales (pd.DataFrame): Datos antes de imputación
        datos_imputados (pd.DataFrame): Datos después de imputación
        
    Returns:
        dict: Resultados de validación operativa
    """
    
    validacion = {}
    
    print("\n=== VALIDACIÓN DE COHERENCIA OPERATIVA ===")
    
    for grupo in datos_originales['Grupo_Operativo'].unique():
        # Datos originales (sin NaN)
        orig_grupo = datos_originales[datos_originales['Grupo_Operativo'] == grupo]['Duracion_min'].dropna()
        
        # Datos imputados (completos)
        imput_grupo = datos_imputados[datos_imputados['Grupo_Operativo'] == grupo]['Duracion_min']
        
        # Calcular diferencias operativas
        diff_media = abs(orig_grupo.mean() - imput_grupo.mean())
        diff_std = abs(orig_grupo.std() - imput_grupo.std())
        diff_mediana = abs(orig_grupo.median() - imput_grupo.median())
        
        # Impacto en productividad
        productividad_orig = 60 / orig_grupo.mean()
        productividad_imput = 60 / imput_grupo.mean()
        diff_productividad = abs(productividad_orig - productividad_imput)
        
        # Porcentaje de datos imputados
        n_total = len(datos_originales[datos_originales['Grupo_Operativo'] == grupo])
        n_faltantes = n_total - len(orig_grupo)
        pct_imputados = (n_faltantes / n_total) * 100
        
        # Verificar valores razonables para call center
        valores_imputados = datos_imputados[
            (datos_imputados['Grupo_Operativo'] == grupo) & 
            (datos_originales[datos_originales['Grupo_Operativo'] == grupo]['Duracion_min'].isna())
        ]['Duracion_min']
        
        # Validar rangos operativos (llamadas entre 1-30 minutos son razonables)
        valores_atipicos = sum((valores_imputados < 1) | (valores_imputados > 30))
        
        print(f"\n{grupo}:")
        print(f"  Datos imputados: {n_faltantes}/{n_total} ({pct_imputados:.1f}%)")
        print(f"  Diferencia en duración promedio: {diff_media:.3f} min")
        print(f"  Diferencia en mediana: {diff_mediana:.3f} min")
        print(f"  Diferencia en variabilidad: {diff_std:.3f} min")
        print(f"  Impacto en productividad: {diff_productividad:.2f} llamadas/hora")
        print(f"  Valores operativamente atípicos: {valores_atipicos}")
        
        # Clasificación de impacto
        if diff_media < 0.1 and diff_productividad < 0.5:
            impacto = "✓ Impacto mínimo"
        elif diff_media < 0.5 and diff_productividad < 1.0:
            impacto = "⚠ Impacto leve"
        else:
            impacto = "✗ Impacto significativo - revisar"
        
        print(f"  Evaluación de impacto: {impacto}")
        
        validacion[grupo] = {
            'n_imputados': n_faltantes,
            'pct_imputados': round(pct_imputados, 1),
            'diff_media': round(diff_media, 3),
            'diff_mediana': round(diff_mediana, 3),
            'diff_std': round(diff_std, 3),
            'diff_productividad': round(diff_productividad, 2),
            'valores_atipicos': valores_atipicos,
            'impacto': impacto
        }
    
    return validacion

def imputar_por_media_operador_turno(datos):
    """
    Imputa valores faltantes usando la media por operador y turno.
    
    Args:
        datos (pd.DataFrame): Dataset con valores faltantes
        
    Returns:
        tuple: (datos_imputados, medias_por_grupo, resumen_imputacion)
    """
    
    datos_imputados = datos.copy()
    medias_por_grupo = {}
    resumen_imputacion = {}
    
    print("\n=== CÁLCULO DE MEDIAS POR OPERADOR Y TURNO ===")
    
    # Calcular medias por grupo operativo
    for grupo in datos['Grupo_Operativo'].unique():
        datos_grupo = datos[datos['Grupo_Operativo'] == grupo]['Duracion_min']
        media_grupo = datos_grupo.mean()  # Automáticamente excluye NaN
        medias_por_grupo[grupo] = media_grupo
        
        # Contar valores faltantes
        n_faltantes = datos_grupo.isna().sum()
        n_total = len(datos_grupo)
        
        # Calcular impacto en productividad
        llamadas_hora = 60 / media_grupo if media_grupo > 0 else 0
        
        print(f"{grupo}:")
        print(f"  Media: {media_grupo:.3f} min")
        print(f"  Productividad: {llamadas_hora:.1f} llamadas/hora")
        print(f"  Imputará: {n_faltantes}/{n_total} valores ({(n_faltantes/n_total)*100:.1f}%)")
        
        resumen_imputacion[grupo] = {
            'media': round(media_grupo, 3),
            'productividad': round(llamadas_hora, 1),
            'n_faltantes': n_faltantes,
            'n_total': n_total,
            'pct_faltantes': round((n_faltantes/n_total)*100, 1)
        }
    
    # Realizar imputación
    print("\n=== PROCESO DE IMPUTACIÓN ===")
    
    for grupo in datos['Grupo_Operativo'].unique():
        mask_grupo = datos_imputados['Grupo_Operativo'] == grupo
        mask_faltantes = datos_imputados['Duracion_min'].isna()
        mask_imputar = mask_grupo & mask_faltantes
        
        if mask_imputar.any():
            datos_imputados.loc[mask_imputar, 'Duracion_min'] = medias_por_grupo[grupo]
            n_imputados = mask_imputar.sum()
            print(f"✓ {grupo}: {n_imputados} llamadas imputadas con {medias_por_grupo[grupo]:.3f} min")
    
    return datos_imputados, medias_por_grupo, resumen_imputacion

def analizar_eficiencia_comparativa(datos):
    """
    Analiza la eficiencia comparativa entre operadores y turnos.
    
    Args:
        datos (pd.DataFrame): Dataset completo después de imputación
        
    Returns:
        dict: Análisis de eficiencia comparativa
    """
    
    print("\n=== ANÁLISIS DE EFICIENCIA COMPARATIVA ===")
    
    eficiencia = {}
    
    # Ranking de operadores por eficiencia
    print("\nRanking de Operadores por Eficiencia:")
    ranking_operadores = datos.groupby('Operador').agg({
        'Duracion_min': ['mean', 'std', 'count']
    }).round(2)
    
    ranking_operadores.columns = ['Duracion_Promedio', 'Variabilidad', 'Total_Llamadas']
    ranking_operadores['Llamadas_Por_Hora'] = (60 / ranking_operadores['Duracion_Promedio']).round(1)
    ranking_operadores['Indice_Eficiencia'] = (
        ranking_operadores['Llamadas_Por_Hora'] / ranking_operadores['Variabilidad']
    ).round(2)
    
    ranking_operadores = ranking_operadores.sort_values('Indice_Eficiencia', ascending=False)
    
    for i, (operador, metricas) in enumerate(ranking_operadores.iterrows(), 1):
        print(f"  {i}. {operador}:")
        print(f"     Duración promedio: {metricas['Duracion_Promedio']} min")
        print(f"     Llamadas/hora: {metricas['Llamadas_Por_Hora']}")
        print(f"     Índice eficiencia: {metricas['Indice_Eficiencia']}")
    
    # Análisis por turnos
    print("\nAnálisis de Carga por Turnos:")
    analisis_turnos = datos.groupby('Franja_Horaria').agg({
        'Duracion_min': ['mean', 'std', 'count']
    }).round(2)
    
    analisis_turnos.columns = ['Duracion_Promedio', 'Variabilidad', 'Total_Llamadas']
    analisis_turnos['Complejidad_Relativa'] = (
        analisis_turnos['Duracion_Promedio'] / analisis_turnos['Duracion_Promedio'].min()
    ).round(2)
    
    for turno, metricas in analisis_turnos.iterrows():
        if metricas['Complejidad_Relativa'] > 1.5:
            complejidad = COMPLEJIDAD_ALTA
        elif metricas['Complejidad_Relativa'] > 1.2:
            complejidad = COMPLEJIDAD_MEDIA
        else:
            complejidad = COMPLEJIDAD_BAJA
            
        print(f"\n{turno}:")
        print(f"  Duración promedio: {metricas['Duracion_Promedio']} min")
        print(f"  Variabilidad: {metricas['Variabilidad']} min")
        print(f"  Complejidad relativa: {metricas['Complejidad_Relativa']}x ({complejidad})")
    
    eficiencia['ranking_operadores'] = ranking_operadores
    eficiencia['analisis_turnos'] = analisis_turnos
    
    return eficiencia

def main():
    """
    Función principal que ejecuta el análisis completo del call center.
    """
    
    print("EJERCICIO 10: IMPUTACIÓN POR MEDIA AGRUPADA POR OPERADOR Y TURNO")
    print("=" * 80)
    
    # 1. Crear datos del call center
    datos_originales = crear_datos_call_center()
    
    print("\nDATOS ORIGINALES DEL CALL CENTER:")
    print(datos_originales.head(15))
    print(f"\nDimensiones: {datos_originales.shape}")
    print(f"Total llamadas: {len(datos_originales)}")
    print(f"Valores faltantes: {datos_originales['Duracion_min'].isna().sum()}")
    
    # 2. Análisis de métricas operativas
    metricas_operativas = analizar_metricas_call_center(datos_originales)
    
    # 3. Análisis de patrones operativos
    _ = analizar_patrones_operativos(datos_originales)
    
    # 4. Análisis de datos faltantes por grupo
    print("\n=== ANÁLISIS DE DATOS FALTANTES POR GRUPO OPERATIVO ===")
    for grupo in datos_originales['Grupo_Operativo'].unique():
        datos_grupo = datos_originales[datos_originales['Grupo_Operativo'] == grupo]
        n_total = len(datos_grupo)
        n_faltantes = datos_grupo['Duracion_min'].isna().sum()
        pct_faltantes = (n_faltantes / n_total) * 100
        
        print(f"{grupo}:")
        print(f"  Total llamadas: {n_total}")
        print(f"  Datos faltantes: {n_faltantes} ({pct_faltantes:.1f}%)")
        print(f"  Datos válidos: {n_total - n_faltantes}")
    
    # 5. Imputación por media de operador y turno
    datos_imputados, _, _ = imputar_por_media_operador_turno(datos_originales)
    
    # 6. Comparación antes/después
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS DE IMPUTACIÓN ===")
    
    for grupo in datos_originales['Grupo_Operativo'].unique():
        datos_orig = datos_originales[datos_originales['Grupo_Operativo'] == grupo]['Duracion_min']
        datos_imput = datos_imputados[datos_imputados['Grupo_Operativo'] == grupo]['Duracion_min']
        
        print(f"\n{grupo}:")
        print("  Datos originales (primeros 10):")
        print(f"    {[f'{x:.1f}' if not pd.isna(x) else 'NaN' for x in datos_orig.head(10).values]}")
        print("  Datos imputados (primeros 10):")
        print(f"    {[f'{x:.3f}' for x in datos_imput.head(10).values]}")
        
        # Estadísticas comparativas
        orig_sin_nan = datos_orig.dropna()
        print(f"  Media original (sin NaN): {orig_sin_nan.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Productividad original: {60/orig_sin_nan.mean():.1f} llamadas/hora")
        print(f"  Productividad imputada: {60/datos_imput.mean():.1f} llamadas/hora")
    
    # 7. Validación operativa
    validacion = validar_coherencia_operativa(datos_originales, datos_imputados)
    
    # 8. Análisis de eficiencia comparativa
    eficiencia = analizar_eficiencia_comparativa(datos_imputados)
    
    # 9. Resumen estadístico final
    print("\n=== RESUMEN ESTADÍSTICO FINAL POR GRUPO OPERATIVO ===")
    resumen_final = datos_imputados.groupby('Grupo_Operativo')['Duracion_min'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(2)
    
    # Agregar productividad
    resumen_final['Llamadas_Hora'] = (60 / resumen_final['mean']).round(1)
    
    print(resumen_final)
    
    # 10. Análisis de distribución de carga de trabajo
    print("\n=== DISTRIBUCIÓN DE CARGA DE TRABAJO ===")
    
    carga_total = datos_imputados.groupby(['Operador', 'Franja_Horaria']).agg({
        'Duracion_min': ['count', 'sum', 'mean']
    }).round(2)
    
    carga_total.columns = ['Num_Llamadas', 'Tiempo_Total_min', 'Duracion_Promedio']
    carga_total['Tiempo_Total_horas'] = (carga_total['Tiempo_Total_min'] / 60).round(2)
    
    print("\nCarga de trabajo por Operador y Turno:")
    print(carga_total)
    
    # 11. Recomendaciones operativas
    print("\n=== RECOMENDACIONES OPERATIVAS ===")
    
    recomendaciones = [
        "1. OPTIMIZACIÓN DE TURNOS:",
        f"   - Turno con mayor eficiencia: {datos_imputados.groupby('Franja_Horaria')['Duracion_min'].mean().idxmin()}",
        f"   - Turno con mayor carga: {datos_imputados.groupby('Franja_Horaria')['Duracion_min'].mean().idxmax()}",
        "",
        "2. GESTIÓN DE OPERADORES:",
        f"   - Operador más eficiente: {eficiencia['ranking_operadores'].index[0]}",
        f"   - Operador con mayor consistencia: {datos_imputados.groupby('Operador')['Duracion_min'].std().idxmin()}",
        "",
        "3. DISTRIBUCIÓN DE RECURSOS:",
        "   - Reforzar turnos de mayor complejidad",
        "   - Capacitación focalizada en eficiencia",
        "   - Monitoreo continuo de métricas por grupo",
        "",
        "4. CONTROL DE CALIDAD:",
        "   - Implementar alertas por duración excesiva",
        "   - Análisis de patrones de llamadas atípicas",
        "   - Seguimiento de tendencias por operador/turno"
    ]
    
    for recomendacion in recomendaciones:
        print(recomendacion)
    
    # 12. Ventajas de la media por operador y turno
    print("\n" + "=" * 80)
    print("VENTAJAS DE LA MEDIA POR OPERADOR Y TURNO")
    print("=" * 80)
    
    ventajas = [
        "1. PRESERVACIÓN DE PATRONES OPERATIVOS:",
        "   - Mantiene características individuales de cada operador",
        "   - Conserva diferencias de carga por franja horaria",
        "   - Respeta variaciones de complejidad temporal",
        "",
        "2. VALIDEZ OPERACIONAL:",
        "   - Basada en experiencia específica del operador",
        "   - Coherente con dinámicas del turno de trabajo",
        "   - Preserva patrones de productividad reales",
        "",
        "3. PRECISIÓN EN MÉTRICAS:",
        "   - Reduce sesgo en KPIs por operador",
        "   - Mantiene representatividad de cada turno",
        "   - Válida para evaluaciones de desempeño",
        "",
        "4. APLICABILIDAD GERENCIAL:",
        "   - Base para decisiones de staffing",
        "   - Útil para planificación de turnos",
        "   - Coherente con evaluaciones individuales",
        "",
        "5. ROBUSTEZ ANALÍTICA:",
        "   - Minimiza distorsión de métricas grupales",
        "   - Preserva variabilidad inter-turno",
        "   - Mantiene poder estadístico para análisis",
        "",
        "6. INTERPRETACIÓN OPERATIVA:",
        "   - Refleja realidades del call center",
        "   - Facilita análisis de eficiencia",
        "   - Base para optimización de procesos",
        "",
        "APLICACIONES ESPECÍFICAS:",
        "- Análisis de productividad individual",
        "- Planificación de recursos humanos",
        "- Evaluación de desempeño por turnos",
        "- Optimización de distribución de carga",
        "- Identificación de necesidades de capacitación"
    ]
    
    for ventaja in ventajas:
        print(ventaja)
    
    # 13. Datos finales
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(datos_imputados)
    print(f"\nValores faltantes después de imputación: {datos_imputados['Duracion_min'].isna().sum()}")
    
    return datos_imputados, metricas_operativas, validacion

if __name__ == "__main__":
    datos_final, metricas, validacion = main()
