# -*- coding: utf-8 -*-
# Ejercicio de Sistema de Recomendaciones de Netflix con IA
# Plataforma de streaming que recomienda películas/canciones usando IA

from fractions import Fraction

# -------------------------------------------------------------
# DATOS DEL PROBLEMA
# -------------------------------------------------------------
# Durante una semana de observación:
# - De 1000 recomendaciones, el usuario realmente disfrutó 300 (valor alto)
# - El sistema clasificó 350 como de alta probabilidad de gusto
# - De esas 350 clasificadas como gustadas, 250 fueron consideradas con gustos realmente altos

total_recomendaciones = 1000
realmente_disfruto = 300        # Recomendaciones que el usuario SÍ disfrutó (valor alto)
sistema_clasifico = 350         # Recomendaciones que el sistema marcó como "alta probabilidad de gusto"
clasificadas_y_disfrutadas = 250  # De las 350 clasificadas, cuántas fueron realmente disfrutadas

# -------------------------------------------------------------
# EVENTOS
# -------------------------------------------------------------
# G = El usuario realmente disfruta la recomendación (Gusto real)
# R = El sistema recomienda como "alta probabilidad de gusto"

# -------------------------------------------------------------
# EJERCICIO 1: P(G) - Probabilidad de que una recomendación sea del gusto
# -------------------------------------------------------------
P_G = realmente_disfruto / total_recomendaciones
P_G_frac = Fraction(realmente_disfruto, total_recomendaciones)

print("="*70)
print("EJERCICIO: SISTEMA DE RECOMENDACIONES DE NETFLIX CON IA")
print("="*70)
print(f"\nTotal de recomendaciones en la semana: {total_recomendaciones:,}")
print(f"Recomendaciones realmente disfrutadas (valor alto): {realmente_disfruto}")
print(f"Recomendaciones clasificadas como 'alta probabilidad': {sistema_clasifico}")
print(f"De las clasificadas, realmente disfrutadas: {clasificadas_y_disfrutadas}")
print("\n" + "-"*70)

print("\n1. P(G) - Probabilidad de que una recomendación sea del gusto del usuario:")
print(f"   P(G) = {realmente_disfruto}/{total_recomendaciones} = {P_G:.6f} = {P_G*100:.2f}%")
print(f"   Fracción simplificada: {P_G_frac}")

# -------------------------------------------------------------
# EJERCICIO 2: P(R) - Probabilidad de que el sistema recomiende como gusta
# -------------------------------------------------------------
P_R = sistema_clasifico / total_recomendaciones
P_R_frac = Fraction(sistema_clasifico, total_recomendaciones)

print("\n2. P(R) - Probabilidad de que el sistema recomiende como gusta:")
print(f"   P(R) = {sistema_clasifico}/{total_recomendaciones} = {P_R:.6f} = {P_R*100:.2f}%")
print(f"   Fracción simplificada: {P_R_frac}")

# -------------------------------------------------------------
# EJERCICIO 3: P(G|R) - Prob. condicional: gusto real SI fue recomendada
# -------------------------------------------------------------
# De las 350 recomendaciones clasificadas como "alta probabilidad", 250 fueron realmente disfrutadas
P_G_dado_R = clasificadas_y_disfrutadas / sistema_clasifico
P_G_dado_R_frac = Fraction(clasificadas_y_disfrutadas, sistema_clasifico)

print("\n3. P(G|R) - Prob. de que realmente guste SI el sistema recomendó:")
print(f"   P(G|R) = {clasificadas_y_disfrutadas}/{sistema_clasifico} = {P_G_dado_R:.6f} = {P_G_dado_R*100:.2f}%")
print(f"   Fracción simplificada: {P_G_dado_R_frac}")
print(f"   Interpretación: De cada 100 recomendaciones del sistema, ~{P_G_dado_R*100:.1f} son realmente disfrutadas")

# -------------------------------------------------------------
# EJERCICIO 4: P(Falso Positivo) - Prob. de recomendar algo que NO gustó
# -------------------------------------------------------------
# Falso Positivo: El sistema recomienda pero el usuario NO disfruta
# Calculemos todos los escenarios:
# - Recomendadas y disfrutadas (G ∩ R): 250
# - Recomendadas pero NO disfrutadas (NoG ∩ R): 350 - 250 = 100 [FALSOS POSITIVOS]
# - NO recomendadas pero SÍ disfrutadas (G ∩ NoR): 300 - 250 = 50 [FALSOS NEGATIVOS]
# - NO recomendadas y NO disfrutadas (NoG ∩ NoR): 1000 - 300 - 100 = 600

recomendadas_no_disfrutadas = sistema_clasifico - clasificadas_y_disfrutadas  # 100 (Falsos Positivos)
no_recomendadas_disfrutadas = realmente_disfruto - clasificadas_y_disfrutadas  # 50 (Falsos Negativos)
no_recomendadas_no_disfrutadas = total_recomendaciones - realmente_disfruto - recomendadas_no_disfrutadas  # 600

total_no_recomendadas = total_recomendaciones - sistema_clasifico  # 650

# P(Falso Positivo) = Recomendaciones que marcó como gustadas pero NO fueron del gusto
# Esto es P(R | NoG) = P(R ∩ NoG) / P(NoG)
total_no_gustadas = total_recomendaciones - realmente_disfruto  # 700

P_Falso_Positivo = recomendadas_no_disfrutadas / total_no_gustadas
P_Falso_Positivo_frac = Fraction(recomendadas_no_disfrutadas, total_no_gustadas)

print("\n4. P(Falso Positivo) - Prob. de que el sistema recomiende algo que NO gustó:")
print(f"   Total de recomendaciones NO disfrutadas: {total_no_gustadas}")
print(f"   Recomendadas pero NO disfrutadas (Falsos Positivos): {recomendadas_no_disfrutadas}")
print(f"   P(R|NoG) = {recomendadas_no_disfrutadas}/{total_no_gustadas} = {P_Falso_Positivo:.6f} = {P_Falso_Positivo*100:.2f}%")
print(f"   Fracción simplificada: {P_Falso_Positivo_frac}")
print(f"   Interpretación: De cada 100 contenidos que NO gustan, ~{P_Falso_Positivo*100:.1f} son recomendados")

# -------------------------------------------------------------
# TABLA PARA VISUALIZACIÓN DE RESULTADOS
# -------------------------------------------------------------
print("\n" + "="*70)
print("TABLA PARA VISUALIZACIÓN DE RESULTADOS")
print("="*70)
print(f"{'':30} | {'Recomendado':>15} | {'No Recomendado':>15} | {'Total':>15}")
print("-"*70)
print(f"{'Gustó (G)':30} | {clasificadas_y_disfrutadas:>15} | {no_recomendadas_disfrutadas:>15} | {realmente_disfruto:>15}")
print(f"{'No Gustó (NoG)':30} | {recomendadas_no_disfrutadas:>15} | {no_recomendadas_no_disfrutadas:>15} | {total_no_gustadas:>15}")
print("-"*70)
print(f"{'Total':30} | {sistema_clasifico:>15} | {total_no_recomendadas:>15} | {total_recomendaciones:>15}")

# -------------------------------------------------------------
# CLASIFICACIÓN DE RESULTADOS
# -------------------------------------------------------------
print("\n" + "="*70)
print("CLASIFICACIÓN DE RESULTADOS")
print("="*70)
print(f"Verdaderos Positivos (VP): {clasificadas_y_disfrutadas}")
print(f"  → Recomendaciones correctas (usuario disfrutó)")
print(f"Falsos Positivos (FP): {recomendadas_no_disfrutadas}")
print(f"  → Malas recomendaciones (usuario NO disfrutó)")
print(f"Falsos Negativos (FN): {no_recomendadas_disfrutadas}")
print(f"  → Oportunidades perdidas (hubiera gustado pero NO se recomendó)")
print(f"Verdaderos Negativos (VN): {no_recomendadas_no_disfrutadas}")
print(f"  → Contenido correctamente NO recomendado")

# -------------------------------------------------------------
# RESUMEN FINAL
# -------------------------------------------------------------
print("\n" + "="*70)
print("RESUMEN DE RESPUESTAS")
print("="*70)
print(f"1. P(G) = {P_G_frac} ≈ {P_G:.6f} ({P_G*100:.2f}%)")
print(f"2. P(R) = {P_R_frac} ≈ {P_R:.6f} ({P_R*100:.2f}%)")
print(f"3. P(G|R) = {P_G_dado_R_frac} ≈ {P_G_dado_R:.6f} ({P_G_dado_R*100:.2f}%)")
print(f"4. P(Falso Positivo) = {P_Falso_Positivo_frac} ≈ {P_Falso_Positivo:.6f} ({P_Falso_Positivo*100:.2f}%)")
print("="*70)