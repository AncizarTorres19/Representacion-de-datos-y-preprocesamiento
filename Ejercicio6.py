"""
Ejercicio 6 - Mediana por región
Imputación de datos faltantes en tamaños de parcelas agrícolas (hectáreas)
por región utilizando la mediana por región ante posible dispersión y outliers.
"""

import pandas as pd
import numpy as np

def crear_datos_parcelas():
    """
    Crea los datos de tamaños de parcelas con valores faltantes según el enunciado
    """
    # Datos de Llanos (20 registros)
    llanos = [50, 60, np.nan, 55, 70, 65, 62, 59, np.nan, 54, 
              66, 63, 68, np.nan, 57, 61, 64, 58, 67, 69]
    
    # Datos de Región Andina (20 registros)
    andina = [20, 25, 28, np.nan, 22, 30, 27, 24, 26, np.nan, 
              29, 23, 21, np.nan, 22, 24, 25, 27, 28, 23]
    
    # Datos de Región Caribe (20 registros)
    caribe = [15, 18, 17, np.nan, 16, 19, 20, 21, np.nan, 22, 
              18, 16, 19, np.nan, 20, 17, 18, 19, 21, np.nan]
    
    # Crear DataFrame
    datos = {
        'Region': ['Llanos'] * 20 + ['Andina'] * 20 + ['Caribe'] * 20,
        'Tamano_Parcela': llanos + andina + caribe
    }
    
    df = pd.DataFrame(datos)
    return df

def imputar_por_mediana_region(df):
    """
    Imputa los valores faltantes utilizando la mediana del tamaño de parcelas por región
    """
    df_imputado = df.copy()
    
    # Calcular la mediana por región (ignorando valores NaN)
    medianas_region = df.groupby('Region')['Tamano_Parcela'].median()
    
    print("=== MEDIANAS DE TAMAÑO DE PARCELAS POR REGIÓN ===")
    for region, mediana in medianas_region.items():
        print(f"Región {region}: {mediana:.1f} hectáreas")
    
    # Imputar valores faltantes con la mediana de cada región
    for region in df['Region'].unique():
        mascara_region = df['Region'] == region
        mascara_nan = df['Tamano_Parcela'].isna()
        mascara_imputar = mascara_region & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Tamano_Parcela'] = medianas_region[region]
    
    return df_imputado, medianas_region

def analizar_dispersion_y_outliers(df):
    """
    Analiza la dispersión de datos y detecta outliers por región
    """
    print("\n=== ANÁLISIS DE DISPERSIÓN Y DETECCIÓN DE OUTLIERS ===")
    
    for region in df['Region'].unique():
        datos_region = df[df['Region'] == region]['Tamano_Parcela'].dropna()
        
        # Estadísticas descriptivas
        media = datos_region.mean()
        mediana = datos_region.median()
        desv_std = datos_region.std()
        
        # Medidas de dispersión
        rango = datos_region.max() - datos_region.min()
        coef_variacion = (desv_std / media) * 100
        
        # Cuartiles y rango intercuartílico
        q1 = datos_region.quantile(0.25)
        q3 = datos_region.quantile(0.75)
        iqr = q3 - q1
        
        # Detección de outliers (método IQR)
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        outliers_moderados = datos_region[(datos_region < limite_inferior) | (datos_region > limite_superior)]
        
        # Outliers extremos (método 3*IQR)
        limite_inf_extremo = q1 - 3 * iqr
        limite_sup_extremo = q3 + 3 * iqr
        outliers_extremos = datos_region[(datos_region < limite_inf_extremo) | (datos_region > limite_sup_extremo)]
        
        # Asimetría
        asimetria = datos_region.skew()
        
        print(f"\nRegión {region}:")
        print(f"  Media: {media:.2f} ha")
        print(f"  Mediana: {mediana:.1f} ha")
        print(f"  Diferencia Media-Mediana: {abs(media - mediana):.2f} ha")
        print(f"  Desviación estándar: {desv_std:.2f} ha")
        print(f"  Coeficiente de variación: {coef_variacion:.1f}%")
        print(f"  Rango: {datos_region.min():.0f} - {datos_region.max():.0f} ha ({rango:.0f} ha)")
        print(f"  Asimetría: {asimetria:.3f}")
        print(f"  Q1: {q1:.1f}, Q3: {q3:.1f}, IQR: {iqr:.1f}")
        print(f"  Límites normales: [{limite_inferior:.1f}, {limite_superior:.1f}]")
        print(f"  Outliers moderados: {len(outliers_moderados)}")
        if len(outliers_moderados) > 0:
            print(f"    Valores: {list(outliers_moderados.round(1))}")
        print(f"  Outliers extremos: {len(outliers_extremos)}")
        if len(outliers_extremos) > 0:
            print(f"    Valores: {list(outliers_extremos.round(1))}")
        
        # Interpretación de dispersión
        if coef_variacion < 15:
            interpretacion_cv = "baja dispersión"
        elif coef_variacion < 30:
            interpretacion_cv = "dispersión moderada"
        else:
            interpretacion_cv = "alta dispersión"
        
        print(f"  Interpretación: {interpretacion_cv}")

def justificar_mediana_vs_media(df):
    """
    Justifica por qué usar mediana en lugar de media para estos datos
    """
    print("\n=== JUSTIFICACIÓN: MEDIANA VS MEDIA ===")
    
    for region in df['Region'].unique():
        datos_region = df[df['Region'] == region]['Tamano_Parcela'].dropna()
        
        media = datos_region.mean()
        mediana = datos_region.median()
        diferencia_porcentual = abs(media - mediana) / mediana * 100
        
        # Simular impacto de outlier
        datos_con_outlier = pd.concat([datos_region, pd.Series([datos_region.max() * 2])])
        media_con_outlier = datos_con_outlier.mean()
        mediana_con_outlier = datos_con_outlier.median()
        
        cambio_media = abs(media_con_outlier - media) / media * 100
        cambio_mediana = abs(mediana_con_outlier - mediana) / mediana * 100
        
        # Detectar outliers reales
        q1 = datos_region.quantile(0.25)
        q3 = datos_region.quantile(0.75)
        iqr = q3 - q1
        outliers = datos_region[(datos_region < q1 - 1.5 * iqr) | (datos_region > q3 + 1.5 * iqr)]
        
        print(f"\nRegión {region}:")
        print(f"  Media actual: {media:.2f} ha")
        print(f"  Mediana actual: {mediana:.1f} ha")
        print(f"  Diferencia relativa: {diferencia_porcentual:.1f}%")
        print(f"  Outliers detectados: {len(outliers)}")
        
        print("  Simulación con outlier extremo:")
        print(f"    Cambio en media: {cambio_media:.1f}%")
        print(f"    Cambio en mediana: {cambio_mediana:.1f}%")
        
        # Recomendación
        if len(outliers) > 0 or diferencia_porcentual > 5:
            recomendacion = "✓ MEDIANA RECOMENDADA"
            razon = "presencia de outliers/asimetría"
        elif diferencia_porcentual < 2:
            recomendacion = "≈ AMBAS APROPIADAS"
            razon = "distribución simétrica"
        else:
            recomendacion = "? EVALUAR CONTEXTO"
            razon = "distribución ligeramente asimétrica"
        
        print(f"  Recomendación: {recomendacion} ({razon})")

def analizar_caracteristicas_regionales(df):
    """
    Analiza las características específicas de cada región agrícola
    """
    print("\n=== CARACTERÍSTICAS AGRÍCOLAS POR REGIÓN ===")
    
    # Estadísticas por región
    for region in df['Region'].unique():
        datos_region = df[df['Region'] == region]['Tamano_Parcela'].dropna()
        
        # Categorizar tamaños de parcelas
        if region == 'Llanos':
            categorias = {
                'Pequeña (<55 ha)': len(datos_region[datos_region < 55]),
                'Mediana (55-65 ha)': len(datos_region[(datos_region >= 55) & (datos_region < 65)]),
                'Grande (≥65 ha)': len(datos_region[datos_region >= 65])
            }
        elif region == 'Andina':
            categorias = {
                'Pequeña (<23 ha)': len(datos_region[datos_region < 23]),
                'Mediana (23-27 ha)': len(datos_region[(datos_region >= 23) & (datos_region < 27)]),
                'Grande (≥27 ha)': len(datos_region[datos_region >= 27])
            }
        else:  # Caribe
            categorias = {
                'Pequeña (<18 ha)': len(datos_region[datos_region < 18]),
                'Mediana (18-20 ha)': len(datos_region[(datos_region >= 18) & (datos_region < 20)]),
                'Grande (≥20 ha)': len(datos_region[datos_region >= 20])
            }
        
        total = len(datos_region)
        mediana = datos_region.median()
        
        print(f"\nRegión {region} (Total: {total} parcelas):")
        print(f"  Mediana: {mediana:.1f} ha")
        
        for categoria, cantidad in categorias.items():
            porcentaje = (cantidad / total) * 100 if total > 0 else 0
            print(f"  {categoria}: {cantidad} parcelas ({porcentaje:.1f}%)")
        
        # Interpretación regional
        if region == 'Llanos':
            print("  Característica: Parcelas extensas para ganadería y cultivos grandes")
        elif region == 'Andina':
            print("  Característica: Parcelas medianas adaptadas a topografía montañosa")
        else:  # Caribe
            print("  Característica: Parcelas más pequeñas para cultivos intensivos")

def comparar_regiones_post_imputacion(df_imputado):
    """
    Compara las regiones después de la imputación
    """
    print("\n=== COMPARACIÓN ENTRE REGIONES (POST-IMPUTACIÓN) ===")
    
    # Estadísticas resumidas
    resumen = df_imputado.groupby('Region')['Tamano_Parcela'].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(2)
    
    print("\nResumen estadístico:")
    print(resumen)
    
    # Ranking por tamaño
    medianas_ordenadas = df_imputado.groupby('Region')['Tamano_Parcela'].median().sort_values(ascending=False)
    
    print("\nRanking por tamaño de parcela (mediana):")
    for i, (region, mediana) in enumerate(medianas_ordenadas.items(), 1):
        print(f"  {i}. Región {region}: {mediana:.1f} hectáreas")
    
    # Análisis de uniformidad
    print("\nAnálisis de uniformidad (menor CV = más uniforme):")
    for region in df_imputado['Region'].unique():
        datos = df_imputado[df_imputado['Region'] == region]['Tamano_Parcela']
        cv = (datos.std() / datos.mean()) * 100
        print(f"  Región {region}: CV = {cv:.1f}%")
    
    # Diferencias entre regiones
    print("\nDiferencias entre regiones:")
    regiones = ['Llanos', 'Andina', 'Caribe']
    for i in range(len(regiones)):
        for j in range(i+1, len(regiones)):
            region1, region2 = regiones[i], regiones[j]
            mediana1 = medianas_ordenadas[region1]
            mediana2 = medianas_ordenadas[region2]
            diferencia = abs(mediana1 - mediana2)
            porcentaje = (diferencia / min(mediana1, mediana2)) * 100
            print(f"  {region1} vs {region2}: {diferencia:.1f} ha ({porcentaje:.1f}% de diferencia)")

def mostrar_resultados(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for region in df_original['Region'].unique():
        datos_region = df_original[df_original['Region'] == region]
        valores_faltantes = datos_region['Tamano_Parcela'].isna().sum()
        total_registros = len(datos_region)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\nRegión {region}:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for region in df_original['Region'].unique():
        print(f"\nRegión {region}:")
        
        # Datos originales
        datos_orig = df_original[df_original['Region'] == region]['Tamano_Parcela']
        datos_imput = df_imputado[df_imputado['Region'] == region]['Tamano_Parcela']
        
        print("  Datos originales:")
        valores_orig = [f"{x:.0f}" if not pd.isna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f"{x:.1f}" for x in datos_imput]
        print(f"    {valores_imput}")
    
    print("\n=== ESTADÍSTICAS DESCRIPTIVAS COMPARATIVAS ===")
    
    for region in df_original['Region'].unique():
        datos_orig = df_original[df_original['Region'] == region]['Tamano_Parcela']
        datos_imput = df_imputado[df_imputado['Region'] == region]['Tamano_Parcela']
        
        print(f"\nRegión {region}:")
        print(f"  Media original (sin NaN): {datos_orig.mean():.3f}")
        print(f"  Media después de imputación: {datos_imput.mean():.3f}")
        print(f"  Mediana original: {datos_orig.median():.1f}")
        print(f"  Mediana después de imputación: {datos_imput.median():.1f}")
        print(f"  Desviación estándar original: {datos_orig.std():.3f}")
        print(f"  Desviación estándar imputada: {datos_imput.std():.3f}")

def explicar_ventajas_mediana_agricola():
    """
    Explica las ventajas específicas de usar mediana en datos agrícolas
    """
    print("\n" + "="*80)
    print("VENTAJAS DE LA MEDIANA PARA DATOS AGRÍCOLAS DE PARCELAS")
    print("="*80)
    print("""
1. ROBUSTEZ ANTE VARIABILIDAD NATURAL:
   - Los tamaños de parcelas varían por factores geográficos y económicos
   - La mediana no se ve afectada por parcelas excepcionalmente grandes o pequeñas
   - Representa mejor el tamaño "típico" de la región
   
2. ADECUADA PARA DISTRIBUCIONES ASIMÉTRICAS:
   - Los datos agrícolas suelen tener distribuciones sesgadas
   - Pocos propietarios con parcelas muy grandes vs muchos con parcelas pequeñas
   - La mediana captura mejor el centro de distribuciones no normales
   
3. RESISTENCIA A OUTLIERS GEOGRÁFICOS:
   - Parcelas atípicas por condiciones especiales (ríos, montañas, urbanización)
   - Latifundios o minifundios excepcionales
   - La mediana mantiene la representatividad regional
   
4. COMPARABILIDAD ENTRE REGIONES:
   - Permite comparaciones justas entre regiones con diferentes características
   - No se distorsiona por las diferencias en variabilidad regional
   - Base sólida para políticas agrícolas regionalizadas
   
5. ESTABILIDAD TEMPORAL:
   - Menos sensible a cambios en el mercado de tierras
   - Robusta ante transacciones excepcionales
   - Útil para análisis longitudinales
   
6. INTERPRETACIÓN PRÁCTICA:
   - 50% de parcelas son menores que la mediana
   - 50% de parcelas son mayores que la mediana
   - Referencia clara para clasificación de productores

APLICACIONES ESPECÍFICAS:
- Políticas de subsidios agrícolas
- Clasificación de pequeños/medianos/grandes productores
- Planificación de infraestructura rural
- Análisis de competitividad regional
    """)

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 6: IMPUTACIÓN POR MEDIANA AGRUPADA POR REGIÓN")
    print("=" * 75)
    
    # Crear datos
    df_original = crear_datos_parcelas()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Analizar dispersión y outliers
    analizar_dispersion_y_outliers(df_original)
    
    # Justificar uso de mediana
    justificar_mediana_vs_media(df_original)
    
    # Analizar características regionales
    analizar_caracteristicas_regionales(df_original)
    
    # Realizar imputación
    df_imputado, _ = imputar_por_mediana_region(df_original)
    
    # Mostrar resultados detallados
    mostrar_resultados(df_original, df_imputado)
    
    # Comparar regiones post-imputación
    comparar_regiones_post_imputacion(df_imputado)
    
    # Explicar ventajas de la mediana
    explicar_ventajas_mediana_agricola()
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Tamano_Parcela'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
