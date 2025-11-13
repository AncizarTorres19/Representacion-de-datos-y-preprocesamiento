# -*- coding: utf-8 -*-
# Ejercicio de Análisis de Radiografías Pulmonares con IA
# Modelo de IA médica para detectar enfermedades pulmonares

from fractions import Fraction

# -------------------------------------------------------------
# DATOS DEL PROBLEMA
# -------------------------------------------------------------
# Base de datos con 5000 imágenes de radiografías:
# - 600 pacientes están realmente enfermos
# - El modelo detecta 700 como positivos
# - Entre los positivos, 540 son realmente enfermos

total_imagenes = 5000
realmente_enfermos = 600        # Pacientes que SÍ tienen la enfermedad
modelo_detecta = 700            # Radiografías marcadas como positivas
positivos_enfermos = 540        # De los 700 positivos, cuántos están realmente enfermos

# -------------------------------------------------------------
# EVENTOS
# -------------------------------------------------------------
# E = El paciente está realmente enfermo
# Pos = El modelo detecta positivo (enfermedad presente)

# -------------------------------------------------------------
# EJERCICIO 1: P(E) - Probabilidad de estar enfermo
# -------------------------------------------------------------
P_E = realmente_enfermos / total_imagenes
P_E_frac = Fraction(realmente_enfermos, total_imagenes)

print("="*70)
print("EJERCICIO: ANÁLISIS DE RADIOGRAFÍAS PULMONARES CON IA")
print("="*70)
print(f"\nTotal de imágenes en base de datos: {total_imagenes:,}")
print(f"Pacientes realmente enfermos: {realmente_enfermos}")
print(f"Radiografías detectadas como positivas: {modelo_detecta}")
print(f"De las positivas, realmente enfermas: {positivos_enfermos}")
print("\n" + "-"*70)

print("\n1. P(E) - Probabilidad de que un paciente esté enfermo:")
print(f"   P(E) = {realmente_enfermos}/{total_imagenes} = {P_E:.6f} = {P_E*100:.2f}%")
print(f"   Fracción simplificada: {P_E_frac}")

# -------------------------------------------------------------
# EJERCICIO 2: P(Pos) - Probabilidad de que el modelo detecte positivo
# -------------------------------------------------------------
P_Pos = modelo_detecta / total_imagenes
P_Pos_frac = Fraction(modelo_detecta, total_imagenes)

print("\n2. P(Pos) - Probabilidad de que el modelo detecte positivo:")
print(f"   P(Pos) = {modelo_detecta}/{total_imagenes} = {P_Pos:.6f} = {P_Pos*100:.2f}%")
print(f"   Fracción simplificada: {P_Pos_frac}")

# -------------------------------------------------------------
# EJERCICIO 3: P(E|Pos) - Prob. condicional: enfermo SI detectó positivo
# -------------------------------------------------------------
# De las 700 radiografías detectadas como positivas, 540 son realmente enfermas
P_E_dado_Pos = positivos_enfermos / modelo_detecta
P_E_dado_Pos_frac = Fraction(positivos_enfermos, modelo_detecta)

print("\n3. P(E|Pos) - Prob. de estar enfermo SI el modelo detectó positivo:")
print(f"   P(E|Pos) = {positivos_enfermos}/{modelo_detecta} = {P_E_dado_Pos:.6f} = {P_E_dado_Pos*100:.2f}%")
print(f"   Fracción simplificada: {P_E_dado_Pos_frac}")
print(f"   Interpretación: De cada 100 positivos detectados, ~{P_E_dado_Pos*100:.1f} están realmente enfermos")

# -------------------------------------------------------------
# EJERCICIO 4: P(Falso Positivo) - Prob. paciente sano detectado como positivo
# -------------------------------------------------------------
# Falso Positivo: El modelo detecta positivo pero el paciente está sano
# Calculemos todos los escenarios:
# - Positivos y enfermos (E ∩ Pos): 540
# - Positivos pero NO enfermos (NoE ∩ Pos): 700 - 540 = 160 [FALSOS POSITIVOS]
# - NO positivos pero SÍ enfermos (E ∩ NoPos): 600 - 540 = 60 [FALSOS NEGATIVOS]
# - NO positivos y NO enfermos (NoE ∩ NoPos): 5000 - 600 - 160 = 4240

positivos_no_enfermos = modelo_detecta - positivos_enfermos  # 160 (Falsos Positivos)
no_positivos_enfermos = realmente_enfermos - positivos_enfermos  # 60 (Falsos Negativos)
no_positivos_no_enfermos = total_imagenes - realmente_enfermos - positivos_no_enfermos  # 4240

total_no_positivos = total_imagenes - modelo_detecta  # 4300

# P(Falso Positivo) = P(Pos ∩ NoE) / P(NoE)
# Número de sanos: 5000 - 600 = 4400
total_sanos = total_imagenes - realmente_enfermos

P_Falso_Positivo = positivos_no_enfermos / total_sanos
P_Falso_Positivo_frac = Fraction(positivos_no_enfermos, total_sanos)

print("\n4. P(Falso Positivo) - Prob. de que un paciente sano sea detectado como positivo:")
print(f"   Total de pacientes sanos: {total_sanos}")
print(f"   Sanos detectados como positivos (Falsos Positivos): {positivos_no_enfermos}")
print(f"   P(Pos|NoE) = {positivos_no_enfermos}/{total_sanos} = {P_Falso_Positivo:.6f} = {P_Falso_Positivo*100:.2f}%")
print(f"   Fracción simplificada: {P_Falso_Positivo_frac}")
print(f"   Interpretación: De cada 100 pacientes sanos, ~{P_Falso_Positivo*100:.1f} son detectados como positivos")

# -------------------------------------------------------------
# TABLA PARA VISUALIZACIÓN DE RESULTADOS
# -------------------------------------------------------------
print("\n" + "="*70)
print("TABLA PARA VISUALIZACIÓN DE RESULTADOS")
print("="*70)
print(f"{'':25} | {'Positivo':>15} | {'Negativo':>15} | {'Total':>15}")
print("-"*70)
print(f"{'Enfermo (E)':25} | {positivos_enfermos:>15} | {no_positivos_enfermos:>15} | {realmente_enfermos:>15}")
print(f"{'Sano (NoE)':25} | {positivos_no_enfermos:>15} | {no_positivos_no_enfermos:>15} | {total_sanos:>15}")
print("-"*70)
print(f"{'Total':25} | {modelo_detecta:>15} | {total_no_positivos:>15} | {total_imagenes:>15}")

# -------------------------------------------------------------
# CLASIFICACIÓN DE RESULTADOS
# -------------------------------------------------------------
print("\n" + "="*70)
print("CLASIFICACIÓN DE RESULTADOS")
print("="*70)
print(f"Verdaderos Positivos (VP): {positivos_enfermos}")
print(f"  → Enfermos correctamente detectados")
print(f"Falsos Positivos (FP): {positivos_no_enfermos}")
print(f"  → Sanos incorrectamente detectados como enfermos")
print(f"Falsos Negativos (FN): {no_positivos_enfermos}")
print(f"  → Enfermos no detectados (casos perdidos)")
print(f"Verdaderos Negativos (VN): {no_positivos_no_enfermos}")
print(f"  → Sanos correctamente identificados")

# -------------------------------------------------------------
# RESUMEN FINAL
# -------------------------------------------------------------
print("\n" + "="*70)
print("RESUMEN DE RESPUESTAS")
print("="*70)
print(f"1. P(E) = {P_E_frac} ≈ {P_E:.6f} ({P_E*100:.2f}%)")
print(f"2. P(Pos) = {P_Pos_frac} ≈ {P_Pos:.6f} ({P_Pos*100:.2f}%)")
print(f"3. P(E|Pos) = {P_E_dado_Pos_frac} ≈ {P_E_dado_Pos:.6f} ({P_E_dado_Pos*100:.2f}%)")
print(f"4. P(Falso Positivo) = {P_Falso_Positivo_frac} ≈ {P_Falso_Positivo:.6f} ({P_Falso_Positivo*100:.2f}%)")
print("="*70)