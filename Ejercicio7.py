"""
Ejercicio 7 - Moda por grupo etario
Imputación de datos faltantes en nivel educativo de base bancaria
por grupo etario utilizando la moda por grupo etario.
"""

import pandas as pd
import numpy as np

# Constantes para niveles educativos
PRIMARIA = "Primaria"
SECUNDARIA = "Secundaria"
TECNICO = "Técnico"
UNIVERSITARIO = "Universitario"
ORDEN_EDUCATIVO = [PRIMARIA, SECUNDARIA, TECNICO, UNIVERSITARIO]
VALORES_NUMERICOS = {PRIMARIA: 1, SECUNDARIA: 2, TECNICO: 3, UNIVERSITARIO: 4}

def crear_datos_educacion():
    """
    Crea los datos de nivel educativo con valores faltantes según el enunciado
    """
    # Datos del grupo 18-30 años (20 registros)
    grupo_18_30 = [UNIVERSITARIO, np.nan, TECNICO, UNIVERSITARIO, SECUNDARIA, 
                   UNIVERSITARIO, np.nan, TECNICO, UNIVERSITARIO, PRIMARIA, 
                   TECNICO, np.nan, SECUNDARIA, UNIVERSITARIO, UNIVERSITARIO, 
                   TECNICO, np.nan, SECUNDARIA, UNIVERSITARIO, TECNICO]
    
    # Datos del grupo 31-50 años (20 registros)
    grupo_31_50 = [SECUNDARIA, UNIVERSITARIO, np.nan, TECNICO, UNIVERSITARIO, 
                   PRIMARIA, SECUNDARIA, UNIVERSITARIO, UNIVERSITARIO, np.nan, 
                   TECNICO, SECUNDARIA, UNIVERSITARIO, np.nan, TECNICO, 
                   UNIVERSITARIO, SECUNDARIA, UNIVERSITARIO, PRIMARIA, np.nan]
    
    # Datos del grupo 51+ años (20 registros)
    grupo_51_mas = [PRIMARIA, SECUNDARIA, SECUNDARIA, np.nan, PRIMARIA, 
                    PRIMARIA, SECUNDARIA, PRIMARIA, PRIMARIA, SECUNDARIA, 
                    np.nan, PRIMARIA, PRIMARIA, SECUNDARIA, PRIMARIA, 
                    PRIMARIA, SECUNDARIA, np.nan, PRIMARIA, PRIMARIA]
    
    # Crear DataFrame
    datos = {
        'Grupo_Etario': ['18-30'] * 20 + ['31-50'] * 20 + ['51+'] * 20,
        'Nivel_Educativo': grupo_18_30 + grupo_31_50 + grupo_51_mas
    }
    
    df = pd.DataFrame(datos)
    return df

def calcular_moda_educativa(serie):
    """
    Calcula la moda para variables categóricas educativas
    """
    serie_limpia = serie.dropna()
    if len(serie_limpia) == 0:
        return np.nan, 0
    
    # Contar frecuencias
    frecuencias = serie_limpia.value_counts()
    if len(frecuencias) == 0:
        return np.nan, 0
    
    moda_valor = frecuencias.index[0]  # El valor más frecuente
    moda_frecuencia = frecuencias.iloc[0]  # Su frecuencia
    
    return moda_valor, moda_frecuencia

def imputar_por_moda_grupo_etario(df):
    """
    Imputa los valores faltantes utilizando la moda del nivel educativo por grupo etario
    """
    df_imputado = df.copy()
    
    # Calcular la moda por grupo etario
    modas_grupo = {}
    frecuencias_moda = {}
    
    print("=== MODAS DE NIVEL EDUCATIVO POR GRUPO ETARIO ===")
    
    for grupo in df['Grupo_Etario'].unique():
        datos_grupo = df[df['Grupo_Etario'] == grupo]['Nivel_Educativo']
        moda_valor, moda_frecuencia = calcular_moda_educativa(datos_grupo)
        
        modas_grupo[grupo] = moda_valor
        frecuencias_moda[grupo] = moda_frecuencia
        
        total_validos = datos_grupo.count()
        porcentaje_moda = (moda_frecuencia / total_validos) * 100 if total_validos > 0 else 0
        
        print(f"Grupo {grupo} años: {moda_valor} (frecuencia: {moda_frecuencia}/{total_validos}, {porcentaje_moda:.1f}%)")
    
    # Imputar valores faltantes con la moda de cada grupo
    for grupo in df['Grupo_Etario'].unique():
        mascara_grupo = df['Grupo_Etario'] == grupo
        mascara_nan = df['Nivel_Educativo'].isna()
        mascara_imputar = mascara_grupo & mascara_nan
        
        df_imputado.loc[mascara_imputar, 'Nivel_Educativo'] = modas_grupo[grupo]
    
    return df_imputado, modas_grupo, frecuencias_moda

def analizar_distribucion_educativa(df):
    """
    Analiza la distribución de niveles educativos por grupo etario
    """
    print("\n=== DISTRIBUCIÓN DE NIVELES EDUCATIVOS POR GRUPO ETARIO ===")
    
    for grupo in df['Grupo_Etario'].unique():
        datos_grupo = df[df['Grupo_Etario'] == grupo]['Nivel_Educativo'].dropna()
        
        print(f"\nGrupo {grupo} años (Total: {len(datos_grupo)} registros válidos):")
        
        # Calcular frecuencias y porcentajes
        frecuencias = datos_grupo.value_counts()
        total = len(datos_grupo)
        
        # Mostrar en orden jerárquico
        for nivel in ORDEN_EDUCATIVO:
            if nivel in frecuencias.index:
                freq = frecuencias[nivel]
                porcentaje = (freq / total) * 100
                print(f"  {nivel}: {freq} personas ({porcentaje:.1f}%)")
            else:
                print(f"  {nivel}: 0 personas (0.0%)")
        
        # Estadísticas adicionales
        nivel_mas_comun = frecuencias.index[0]
        freq_mas_comun = frecuencias.iloc[0]
        porcentaje_dominante = (freq_mas_comun / total) * 100
        
        print(f"  Nivel dominante: {nivel_mas_comun} ({porcentaje_dominante:.1f}%)")
        print(f"  Diversidad educativa: {len(frecuencias)} niveles diferentes")

def verificar_multimodalidad_educativa(df):
    """
    Verifica casos de multimodalidad en los datos educativos
    """
    print("\n=== VERIFICACIÓN DE MULTIMODALIDAD EDUCATIVA ===")
    
    for grupo in df['Grupo_Etario'].unique():
        datos_grupo = df[df['Grupo_Etario'] == grupo]['Nivel_Educativo'].dropna()
        frecuencias = datos_grupo.value_counts()
        
        if len(frecuencias) == 0:
            continue
            
        max_frecuencia = frecuencias.max()
        
        # Encontrar todos los valores con la frecuencia máxima
        modas = frecuencias[frecuencias == max_frecuencia].index.tolist()
        
        print(f"\nGrupo {grupo} años:")
        if len(modas) == 1:
            print(f"  ✓ Unimodal: {modas[0]} (frecuencia: {max_frecuencia})")
        else:
            print(f"  ⚠ Multimodal: {modas} (frecuencia: {max_frecuencia} cada uno)")
            print("    En caso multimodal, se selecciona el primer valor en orden alfabético")

def analizar_patrones_generacionales(df):
    """
    Analiza los patrones educativos generacionales
    """
    print("\n=== ANÁLISIS DE PATRONES EDUCATIVOS GENERACIONALES ===")
    
    for grupo in df['Grupo_Etario'].unique():
        datos_grupo = df[df['Grupo_Etario'] == grupo]['Nivel_Educativo'].dropna()
        
        # Calcular nivel educativo promedio (numérico)
        valores_num = [VALORES_NUMERICOS[nivel] for nivel in datos_grupo]
        promedio_numerico = np.mean(valores_num)
        
        # Distribución por categorías
        frecuencias = datos_grupo.value_counts()
        total = len(datos_grupo)
        
        # Calcular concentración en educación superior (Técnico + Universitario)
        educ_superior = frecuencias.get(TECNICO, 0) + frecuencias.get(UNIVERSITARIO, 0)
        porcentaje_superior = (educ_superior / total) * 100
        
        # Calcular concentración en educación básica (Primaria + Secundaria)
        educ_basica = frecuencias.get(PRIMARIA, 0) + frecuencias.get(SECUNDARIA, 0)
        porcentaje_basica = (educ_basica / total) * 100
        
        print(f"\nGrupo {grupo} años:")
        print(f"  Nivel educativo promedio: {promedio_numerico:.2f}")
        print(f"  Educación superior (Técnico+Universitario): {porcentaje_superior:.1f}%")
        print(f"  Educación básica (Primaria+Secundaria): {porcentaje_basica:.1f}%")
        
        # Interpretación generacional
        if grupo == '18-30':
            interpretacion = "Generación con mayor acceso a educación superior"
        elif grupo == '31-50':
            interpretacion = "Generación de transición educativa"
        else:  # 51+
            interpretacion = "Generación con limitado acceso histórico a educación superior"
        
        print(f"  Característica generacional: {interpretacion}")

def mostrar_resultados_imputacion(df_original, df_imputado):
    """
    Muestra los resultados del proceso de imputación
    """
    print("\n=== ANÁLISIS DE DATOS FALTANTES ===")
    
    for grupo in df_original['Grupo_Etario'].unique():
        datos_grupo = df_original[df_original['Grupo_Etario'] == grupo]
        valores_faltantes = datos_grupo['Nivel_Educativo'].isna().sum()
        total_registros = len(datos_grupo)
        porcentaje_faltantes = (valores_faltantes / total_registros) * 100
        
        print(f"\nGrupo {grupo} años:")
        print(f"  - Valores faltantes: {valores_faltantes}/{total_registros} ({porcentaje_faltantes:.1f}%)")
        print(f"  - Valores válidos antes: {total_registros - valores_faltantes}")
        print(f"  - Valores válidos después: {total_registros}")
    
    print("\n=== COMPARACIÓN ANTES Y DESPUÉS ===")
    
    for grupo in df_original['Grupo_Etario'].unique():
        print(f"\nGrupo {grupo} años:")
        
        # Datos originales
        datos_orig = df_original[df_original['Grupo_Etario'] == grupo]['Nivel_Educativo']
        datos_imput = df_imputado[df_imputado['Grupo_Etario'] == grupo]['Nivel_Educativo']
        
        print("  Datos originales:")
        valores_orig = [f'"{x}"' if pd.notna(x) else "NaN" for x in datos_orig]
        print(f"    {valores_orig}")
        
        print("  Datos imputados:")
        valores_imput = [f'"{x}"' for x in datos_imput]
        print(f"    {valores_imput}")

def analizar_cambios_distribucionales(df_original, df_imputado):
    """
    Analiza cómo cambia la distribución tras la imputación
    """
    print("\n=== ANÁLISIS DE CAMBIOS DISTRIBUCIONALES ===")
    
    for grupo in df_original['Grupo_Etario'].unique():
        print(f"\nGrupo {grupo} años:")
        
        # Datos antes y después
        datos_orig = df_original[df_original['Grupo_Etario'] == grupo]['Nivel_Educativo'].dropna()
        datos_imput = df_imputado[df_imputado['Grupo_Etario'] == grupo]['Nivel_Educativo']
        
        # Frecuencias antes y después
        freq_orig = datos_orig.value_counts().sort_index()
        freq_imput = datos_imput.value_counts().sort_index()
        
        print("  Cambios en frecuencias:")
        for nivel in ORDEN_EDUCATIVO:
            orig_count = freq_orig.get(nivel, 0)
            imput_count = freq_imput.get(nivel, 0)
            cambio = imput_count - orig_count
            
            if cambio > 0:
                print(f"    {nivel}: {orig_count} → {imput_count} (+{cambio})")
            elif cambio == 0:
                print(f"    {nivel}: {orig_count} → {imput_count} (sin cambio)")
            else:
                print(f"    {nivel}: {orig_count} → {imput_count} ({cambio})")
        
        # Calcular preservación de la moda
        moda_orig = datos_orig.mode().iloc[0] if len(datos_orig.mode()) > 0 else "N/A"
        moda_imput = datos_imput.mode().iloc[0] if len(datos_imput.mode()) > 0 else "N/A"
        
        print(f"  Moda original: {moda_orig}")
        print(f"  Moda post-imputación: {moda_imput}")
        print(f"  Preservación de moda: {'✓ Sí' if moda_orig == moda_imput else '✗ No'}")

def comparar_grupos_post_imputacion(df_imputado):
    """
    Compara los grupos etarios después de la imputación
    """
    print("\n=== COMPARACIÓN ENTRE GRUPOS ETARIOS (POST-IMPUTACIÓN) ===")
    
    # Crear tabla de contingencia
    tabla_contingencia = pd.crosstab(df_imputado['Grupo_Etario'], 
                                    df_imputado['Nivel_Educativo'], 
                                    normalize='index') * 100
    
    print("\nDistribución porcentual por grupo etario:")
    print(tabla_contingencia.round(1))
    
    # Ranking por nivel educativo
    print("\nNivel educativo dominante por grupo:")
    for grupo in df_imputado['Grupo_Etario'].unique():
        datos_grupo = df_imputado[df_imputado['Grupo_Etario'] == grupo]['Nivel_Educativo']
        moda_grupo = datos_grupo.mode().iloc[0]
        frecuencia = (datos_grupo == moda_grupo).sum()
        porcentaje = (frecuencia / len(datos_grupo)) * 100
        
        print(f"  Grupo {grupo}: {moda_grupo} ({porcentaje:.1f}%)")

def explicar_ventajas_moda_categorica():
    """
    Explica las ventajas específicas de usar moda para variables categóricas
    """
    print("\n" + "="*80)
    print("VENTAJAS DE LA MODA PARA VARIABLES CATEGÓRICAS EDUCATIVAS")
    print("="*80)
    print("""
1. ÚNICA MEDIDA APROPIADA PARA DATOS CATEGÓRICOS:
   - Los niveles educativos son variables categóricas ordinales
   - La media y mediana no tienen sentido para categorías
   - La moda es la única medida de tendencia central válida
   
2. PRESERVA LA NATURALEZA CATEGÓRICA:
   - Solo utiliza valores que realmente existen en los datos
   - No introduce categorías artificiales o intermedias
   - Mantiene la coherencia del sistema educativo
   
3. REPRESENTA EL COMPORTAMIENTO TÍPICO:
   - Refleja el nivel educativo más común del grupo
   - Útil para perfiles socioeconómicos y demográficos
   - Base para segmentación de mercados bancarios
   
4. INTERPRETACIÓN DIRECTA:
   - Fácil de comunicar: "el nivel educativo más frecuente"
   - Relevante para políticas de inclusión financiera
   - Comprensible para análisis de riesgo crediticio
   
5. ROBUSTA ANTE CAMBIOS MENORES:
   - Pequeñas variaciones no afectan la moda
   - Estable ante errores de codificación aislados
   - Mantiene la característica dominante del grupo
   
6. COHERENCIA GENERACIONAL:
   - Refleja patrones educativos de cada cohorte etaria
   - Considera contexto histórico de acceso educativo
   - Apropiada para análisis sociológicos

APLICACIONES ESPECÍFICAS EN BANCA:
- Segmentación de clientes por perfil educativo
- Diseño de productos financieros específicos
- Evaluación de riesgo crediticio
- Estrategias de inclusión financiera
- Análisis de mercado objetivo
    """)

def main():
    """
    Función principal que ejecuta el ejercicio completo
    """
    print("EJERCICIO 7: IMPUTACIÓN POR MODA AGRUPADA POR GRUPO ETARIO")
    print("=" * 75)
    
    # Crear datos
    df_original = crear_datos_educacion()
    
    # Mostrar datos originales
    print("\nDATOS ORIGINALES:")
    print(df_original)
    
    # Analizar distribución educativa
    analizar_distribucion_educativa(df_original)
    
    # Verificar multimodalidad
    verificar_multimodalidad_educativa(df_original)
    
    # Analizar patrones generacionales
    analizar_patrones_generacionales(df_original)
    
    # Realizar imputación
    df_imputado, modas, frecuencias = imputar_por_moda_grupo_etario(df_original)
    
    # Mostrar resultados de imputación
    mostrar_resultados_imputacion(df_original, df_imputado)
    
    # Analizar cambios distribucionales
    analizar_cambios_distribucionales(df_original, df_imputado)
    
    # Comparar grupos post-imputación
    comparar_grupos_post_imputacion(df_imputado)
    
    # Explicar ventajas de la moda
    explicar_ventajas_moda_categorica()
    
    print("\n=== DATOS FINALES IMPUTADOS ===")
    print(df_imputado)
    
    # Verificar que no quedan valores faltantes
    valores_faltantes_final = df_imputado['Nivel_Educativo'].isna().sum()
    print(f"\nValores faltantes después de imputación: {valores_faltantes_final}")
    
    # Resumen final
    print("\n=== RESUMEN FINAL DE IMPUTACIÓN ===")
    for grupo, moda in modas.items():
        freq = frecuencias[grupo]
        print(f"Grupo {grupo}: Imputado con '{moda}' (moda con {freq} ocurrencias)")
    
    return df_imputado

if __name__ == "__main__":
    df_resultado = main()
